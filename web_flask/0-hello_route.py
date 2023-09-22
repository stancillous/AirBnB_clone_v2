#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    """func to serve the above route"""
    return "Hello HBNB!"


app.run(host="0.0.0.0", port=5000)
