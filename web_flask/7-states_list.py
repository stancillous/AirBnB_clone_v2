#!/usr/bin/python3
"""script to start a flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

states = storage.all(State)  # returns a dict
states_values = states.values()  # a should be  a list

app = Flask("__name__")


@app.route("/states_list", strict_slashes=False)
def states_list():
    """func to serve the above route"""
    return render_template('7-states_list.html', states_val=states_values)


@app.teardown_appcontext
def remove_session(exception):
    """func to remove the current Session after every request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
