#!/usr/bin/python3
"""
Create a simple flask app with a route
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    Root route

    Returns:
        str: Hello HBNB
    """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb route

    Returns:
        str: HBNB
    """

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    Variable rules by user

    Returns:
        str: C {text by user}
    """
    text = text.replace("_", " ")
    return "C {}".format(escape(text))


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """
    Variable rules by user, provide defaults

    Returns:
        str: Python {text by user}
    """
    text = text.replace("_", " ")
    return "Python {}".format(escape(text))


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    app.run(host=host, port=port)
