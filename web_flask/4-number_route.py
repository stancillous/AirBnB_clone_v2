#!/usr/bin/python3
"""python script that starts a Flask web application"""
from flask import Flask

app = Flask("__name__")


@app.route("/number/<int:n>", strict_slashes = False)
def is_it_a_number(n):
    """function to serve the above route"""
    return "%d is a number" %n


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
