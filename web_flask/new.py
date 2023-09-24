#!/usr/bin/python3
""""script to start a flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

# get all states
states = storage.all(State).values()
sorted_values = sorted(states, key=lambda x: x.name)

# for item in sorted_values:
#     print(type(item))
#     print(type(item.id))
#     print("item = ", item)
#     print("item id = ", item.id)

# id = "421a55f4-7d82-47d9-b54c-a76916479555"

# for state in sorted_values:
#     if id == state.id:
#         print("found ", state)

@app.route("/states", strict_slashes=False)
def states():
    """func to serve the above route"""
    return render_template('7-states_list.html', states_val=sorted_values)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """func to serve above route"""

    # get the state instance with that id
    for state in sorted_values:
        if id == state.id:
            return render_template('9-states.html', state_val=state, id_present=True)
    
    return render_template('9-states.html', id_present=False)


@app.teardown_appcontext
def remove_session(exception):
    """removes current session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
