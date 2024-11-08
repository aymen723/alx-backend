#!/usr/bin/env python3
"""
Flask application for rendering templates with Babel for localization and timezone support
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import timezone as tmzn
from pytz import timezone
import pytz.exceptions
from typing import Dict, Union


class Config(object):
    """
    Configuration settings for Babel including languages and default locale/timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Initialize Flask application and configure it with Babel settings
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

# Sample user database with locale and timezone information
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Retrieve user data based on 'login_as' parameter from request arguments
    Returns a user dictionary if found, otherwise returns None
    """
    id = request.args.get('login_as', None)
    if id and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    Set the user in Flask's global object 'g' if found
    This function runs before each request
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Determine the best-matched language for the user
    Checks URL parameters, user settings, and request headers
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    if g.user:
        loc = g.user.get('locale')
        if loc and loc in app.config['LANGUAGES']:
            return loc
    loc = request.headers.get('locale', None)
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Determine the appropriate timezone for the user
    Checks URL parameters, user settings, and defaults to configured timezone
    """
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    dflt = app.config['BABEL_DEFAULT_TIMEZONE']
    return dflt


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handle requests to the root URL and render the main template
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
