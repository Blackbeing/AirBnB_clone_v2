#!/usr/bin/python3
"""
Create a simple flask app with a route
"""
from flask import Flask

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


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    app.run(host=host, port=port)
