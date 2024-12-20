#!/usr/bin/env python3
"""
Flask application with Babel for localization support
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

# User data with locale and timezone preferences
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Configuration class for Babel with supported languages and defaults
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Initialize Flask app and load configuration settings
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    Retrieve user data based on the 'login_as' URL parameter.
    Returns the user dictionary if found, otherwise returns None.
    """
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    Set the user in Flask's global 'g' object before handling the request.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Determine the best matching language based on request parameters
    and supported languages.
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handle requests to the root URL and render the main template.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
