import datetime, os, json
from utilities import constants, utils
from services import scrapper, settings

def canTrade():
    DATA = constants.DATA_FILE
    data_dict = {}

    # Obtenir la donnée
    if dataExists():
        # print('signal.canTrade :: Data exists !')
        data_dict = loadData()
        if not dataIsUpToDate(data_dict):
            scrapper.scrapMainTable()
            data_dict = loadData()
    else:
        # print('signal.canTrade :: Data does not exists ! Scrap and create file')
        scrapper.scrapMainTable()
        data_dict = loadData()

    # Récupère les events de la journée
    investing_events = data_dict["events"]

    canTakeOrders = True
    # Selon l'heure, calculer la réponse
    for event in investing_events:
        timeDelta = compareWithCurentTime(event)
        absDeltaInSeconds = abs(timeDelta.total_seconds())
        # 1800 seconds = 30 minutes
        if (absDeltaInSeconds <= 1800):
            canTakeOrders = False

    return canTakeOrders

def compareWithCurentTime(event):
        decalageValue = settings.getSetting(constants.DECALAGE_HORAIRE)

        event_hour = event['time'].split(':')[0]
        event_minute = event['time'].split(':')[1]

        # On modifie l'heure serveur avec le décalage horaire enregistré
        nowDateTime = datetime.datetime.now() + datetime.timedelta(hours=decalageValue)

        eventDateTime = datetime.datetime(nowDateTime.year, nowDateTime.month, nowDateTime.day, int(event_hour), int(event_minute), 0)

        return (nowDateTime - eventDateTime)

def loadData():
    DATA = constants.DATA_FILE
    # Load data from file
    with open(DATA) as json_file:
        data = json.load(json_file)
        return data

def dataExists():
    DATA = constants.DATA_FILE
    if (os.path.exists(DATA)):
        return True
    else:
        return False

def dataIsUpToDate(dict):
    today = utils.getToday()
    if (dict["date"] == today):
        # print("signal.dataIsUpToDate :: Data is up to date !")
        return True
    else:
        # print("signal.dataIsUpToDate :: Data is not up to date !")
        return False
