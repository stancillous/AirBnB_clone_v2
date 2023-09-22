#!/usr/bin/python3
"""python script that starts a Flask web application"""
from flask import Flask

app = Flask("__name__")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """func to serve the above routes"""
    new_text = text.replace('_', ' ')
    return "python % s" % new_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
