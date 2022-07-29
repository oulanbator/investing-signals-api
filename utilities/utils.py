import datetime
from time import time


def getToday():
    myDatetime = datetime.datetime.now()
    today = str(myDatetime.year) + "/" + str(myDatetime.month) + "/" + str(myDatetime.day)
    return today

def getTimeNow():
    myDatetime = datetime.datetime.now()
    timenow = str(myDatetime.hour) + ":" + str(myDatetime.minute) + ":" + str(myDatetime.second)
    return timenow