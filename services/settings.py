from utilities import constants, utils

def addSetting(key, value):
    PATH = constants.SETTINGS

    # Load
    settings = utils.loadJsonDict(PATH)
    # Update
    settings[key] = value
    # Save
    utils.saveJsonDict(settings, PATH, "Setting saved")

def getSettings(): 
    PATH = constants.SETTINGS
    return utils.loadJsonDict(PATH)

def getSetting(key): 
    PATH = constants.SETTINGS
    settings = utils.loadJsonDict(PATH)
    return settings[key]




