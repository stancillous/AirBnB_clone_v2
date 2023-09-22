#!/usr/bin/python3
"""python script that starts a Flask web application"""
from flask import Flask

app = Flask("__name__")


@app.route("/c/<text>", strict_slashes = False)
def c(text):
    """func to serve the above route"""
    new_text = text.replace('_', ' ')
    return "C %s" %new_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
