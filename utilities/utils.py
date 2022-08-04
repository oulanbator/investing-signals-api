import datetime, json
from services import settings
from utilities import constants


def getToday():
    myDatetime = datetime.datetime.now()
    result = str(myDatetime.year) + "/" + str(myDatetime.month) + "/" + str(myDatetime.day)
    return result

def getTimeNow():
    myDatetime = datetime.datetime.now()
    result = str(myDatetime.hour) + ":" + str(myDatetime.minute) + ":" + str(myDatetime.second)
    return result

def getModifiedTimeNow():
    decalageValue = settings.getSetting(constants.DECALAGE_HORAIRE)

    myDatetime = datetime.datetime.now()
    modifiedTime = myDatetime + datetime.timedelta(hours=decalageValue)

    result = str(modifiedTime.hour) + ":" + str(modifiedTime.minute) + ":" + str(modifiedTime.second)
    return result


def loadJsonDict(file_path):
    with open(file_path) as json_file:
        dictionnary = json.load(json_file)
        return dictionnary

def saveJsonDict(dictionnary, file_path, message):
    with open(file_path, 'w') as output:
        json.dump(dictionnary, output, indent=4)
        if (message != ""):
            print('jsonutils.saveJsonDict ::' + message + ' !')