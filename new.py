#!/usr/bin/python3
""""script to start a flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

# get all states
states = storage.all(State).values()
sorted_values = sorted(states, key=lambda x: x.name)

ids = []
for item in sorted_values:
    ids.append(item.id)

@app.route("/states", strict_slashes=False)
def states():
    """func to serve the above route"""
    return render_template('7-states_list.html', states_vals=sorted_values)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """func to serve above route"""
    if id in ids:
        return render_template('9-states.html', id_present=True, states=sorted_values)
    else:
        return render_template('9-states.html', id_present=False)


@app.teardown_appcontext
def remove_session(exception):
    """removes current session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
