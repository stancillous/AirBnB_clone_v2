#!/usr/bin/python3
from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def hello():
    """func to serve the above route"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes = False)
def hbnb():
    """func to serve the above route"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes = False)
def c(text):
    """func to serve the above route"""
    new_text = text.replace('_', ' ')
    return "C %s" %new_text

@app.route("/python", strict_slashes = False)
@app.route("/python/<text>", strict_slashes = False)
def python(text = "is cool"):
    """func to serve the above routes"""
    new_text = text.replace('_', ' ')
    return "python %s" %new_text

@app.route("/number/<int:n>", strict_slashes = False)
def is_it_a_number(n):
    """function to serve the above route"""
    return "%d is a number" %n

@app.route("/number_template/<int:n>", strict_slashes = False)
def number_template(n):
    """function to serve the above route"""
    return render_template('5-number.html', num = n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes = False)
def odd_or_even(n):
    """function to serve the above route"""
    return render_template('6-number_odd_or_even.html', num = n)
