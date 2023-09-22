#!/usr/bin/python3
"""python script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask("__name__")


@app.route("/number_odd_or_even/<int:n>", strict_slashes = False)
def odd_or_even(n):
    """function to serve the above route"""
    return render_template('6-number_odd_or_even.html', num = n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
