#!/usr/bin/python3
"""python script that starts a Flask web application"""
from flask import Flask

app = Flask("__name__")


@app.route("/")
def hello():
    """func to serve the above route"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
