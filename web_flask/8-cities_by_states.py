#!/usr/bin/python3
"""script that starts a flask web application"""
import os
from flask import Flask, render_template
from models import storage
from models.state import State
from models.engine.db_storage import DBStorage

app = Flask(__name__)

if os.environ.get("HBNB_TYPE_STORAGE") == "db":
    states_values = storage.all(State).values()
else:
    states_values = storage.all(State)

sorted_states = sorted(states_values, key=lambda x: x.name)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """load states with the cities related to them"""
    return render_template('8-cities_by_states.html', states_val=sorted_states)


@app.teardown_appcontext
def remove_session(exception):
    """func to remove current sqlalchemy sessiono after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
