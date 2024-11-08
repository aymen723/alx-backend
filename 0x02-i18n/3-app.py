#!/usr/bin/env python3
"""
Flask application with Babel integration for language localization
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Configuration class for Babel.
    This sets up the supported languages, default locale, and default timezone.
    """
    LANGUAGES = ["en", "fr"]  # Supported languages for the app
    BABEL_DEFAULT_LOCALE = "en"  # Default language setting
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone setting


# Initialize Flask app and apply the configuration from the Config class
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)  # Initialize Babel for the app


@babel.localeselector
def get_locale():
    """
    Determines the best language to use for a request.
    This function uses the 'Accept-Language' header from the incoming request
    to select the best match for the supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles requests to the root URL and renders the main template.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    # Run the Flask application on port 5000, accessible from any host, with debugging enabled
    app.run(port="5000", host="0.0.0.0", debug=True)
