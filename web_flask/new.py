
from models import storage
from models.state import State
from models.city import City
from models.engine.db_storage import DBStorage

states = storage.all(State)
print(states.values())

newsession = DBStorage.__session
newsession.query(City)
