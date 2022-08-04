import os
import json

from utilities import constants, utils
from services import registry

def addEntry(action):
    PATH = constants.REGISTRY
    DATE = utils.getToday()
    TIME = utils.getTimeNow()

    # Create registry
    createRegistryIfNeeded()
    
    # Load registry
    registry = utils.loadJsonDict(PATH)

    # Update registry
    newEntry = {
        str(len(registry)):  {
            "action": action,
            "date": DATE,
            "time": TIME
        }
    }
    registry.update(newEntry)

    # Save registry
    utils.saveJsonDict(registry, PATH, "Registry updated")


def createRegistryIfNeeded():
    PATH = constants.REGISTRY
    file_exists = os.path.exists(PATH)
    if not file_exists:
        content = {}
        with open(PATH, 'w') as output:
            json.dump(content, output, indent=4)
        print('registry.createRegistryIfNeeded :: Registry created !')

def deleteRegistry():
    PATH = constants.REGISTRY
    file_exists = os.path.exists(PATH)
    if file_exists:
        os.remove(PATH)
        print('registry.deleteRegistry :: Registry deleted !')
