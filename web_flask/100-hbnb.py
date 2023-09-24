#!/usr/bin/python3
""""script to start a flask web app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)

# get all states
states = storage.all(State).values()

# get all amenities
amenities = storage.all(Amenity).values()

# get all places
places = storage.all(Place).values()

sorted_states = sorted(states, key=lambda x: x.name)
sorted_amenities = sorted(amenities, key=lambda x: x.name)
sorted_places = sorted(places, key=lambda x: x.name)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """func to serve the above route"""
    return render_template('100-hbnb.html', places=sorted_places, states=sorted_states, amenities=sorted_amenities)
@app.teardown_appcontext
def remove_session(exception):
    """removes current session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
