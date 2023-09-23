
import os
print("ok")

# # Print environment variables
# print("HBNB_MYSQL_USER:", os.environ.get("HBNB_MYSQL_USER"))
# print("HBNB_MYSQL_PWD:", os.environ.get("HBNB_MYSQL_PWD"))
# print("HBNB_MYSQL_HOST:", os.environ.get("HBNB_MYSQL_HOST"))
# print("HBNB_MYSQL_DB:", os.environ.get("HBNB_MYSQL_DB"))

from models import storage
from models.state import State
from models.city import City
states = storage.all(State)
# print("states is ", states)

for k, v in states.items():
    print(f"{k} = {v}")

for item in states.values():
    print(item.name)
