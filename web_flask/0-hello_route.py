#!/usr/bin/python3
"""Starts a Flask web appliclation.

the application listens on 0.0.0.0, poort 5000.
Routes:
    /:Display  'Hello HNBN!'
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home()
    """This is the home page of the website"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
