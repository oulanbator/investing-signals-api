from bs4 import BeautifulSoup as bs
import requests
import json

from utilities import constants, utils
from services import registry


def scrapMainTable():
    # Constants
    HEADERS = constants.HEADERS
    URL = constants.MAIN_URL
    DATA_FILE = constants.DATA_FILE


    # Request with context manager
    with requests.Session() as session:
        # Send request
        response = session.get(URL, headers=HEADERS)


    # Get BS4 object
    soup = bs(response.content, 'lxml')
    # Get main table and rows
    main_table = soup.find('table', {'id':'economicCalendarData'})
    rows = main_table.find('tbody').findAll('tr', {'class':'js-event-item'})

    # Get data from table
    rows_data = []
    if len(rows) > 0:
        for row in rows:
            # Time
            full_datetime = row['data-event-datetime']
            time = row.find('td', {'class':'time'}).text.strip()
            # Currency
            currency = row.find('td', {'class':'flagCur'}).text.strip()
            # Importance
            sentiment = row.find('td', {'class':'sentiment'})
            stars = sentiment.findAll('i', {'class':'grayFullBullishIcon'})
            importance = len(stars)
            # Title
            event = row.find('td', {'class':'event'}).find('a').text.strip()

            if(currency == 'USD' and importance == 3):
                row_dict = {
                    'datetime': full_datetime,
                    'time': time,
                    'currency': currency,
                    'importance': importance,
                    'event': event
                }
                rows_data.append(row_dict)

    # Prepare data to be saved in a file
    data = {
        "date": utils.getToday(),
        "events": rows_data
    }

    # Save data to file
    with open(DATA_FILE, 'w') as output:
        json.dump(data, output, indent=4)

    registry.addEntry("Scrap data from investing")