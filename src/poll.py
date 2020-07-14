import os
import time
import pandas as pd
from datetime import datetime
from datetime import timedelta
from lxml import html
import requests
from urllib.request import urlopen

cmd = "./run"
time_between = 10 * 60  # in seconds
start_checking = 14 # hour of day after which the script will check for new data
data_input_fname = "./data/DailyConfirmedCases.xlsx"
url = 'https://www.gov.uk/guidance/coronavirus-covid-19-information-for-the-public'

done = False
while True:
    tnow = datetime.now().time()
    print('Taking a look at {:%H:%M}'.format(tnow))

    # Read spread sheet data
    ss = pd.read_excel(data_input_fname)
    ss_last = ss.iloc[-1] # Last row
    last_date = ss_last['DateVal']

    # Retrieve website
    page = str(requests.get(url).content)
    # Get a list of data frames containing tables
    dfl = pd.read_html(page)

    # Read deaths and Pillar 1 positive tests NB: Dependant on table struct
    new_deaths = dfl[0]['Daily'][0]
    new_cases = dfl[1]['Daily'][0]

    # Find date of data NB: This section is very dependant on website
    date_str = page.partition('Positive cases')[2]
    date_str = date_str.partition('As of')[2]
    # date_str = date_str.partition('on')[2].partition(',')[0].strip()
    date_str = date_str.partition('9am')[2].partition(',')[0].strip()
    # Make provision that they sometimnes omit the 'on'
    if (date_str[0] == 'o'):
        date_str = date_str.partition('on')[2].partition(',')[0].strip()
    date_str += ' ' + str(datetime.today().year)
    page_date = datetime.strptime(date_str, '%d %B %Y')

    # If the last dat in the spreadsheet is smaller than the date
    # on the web page then update spreadsheet if there is only one day missing
    if last_date.to_pydatetime() < page_date:
        new_date = last_date + timedelta(days=1)
        if new_date.to_pydatetime() == page_date:
            print('Updating spreadsheet')
            new_ss = ss.append({'DateVal': new_date, 'CMODateCount': new_cases,
                                'DailyDeaths': new_deaths},  ignore_index=True)

            new_ss.to_excel(data_input_fname, index=False)

            print('Running curve_fit', datetime.now())
            returned_value = os.system(cmd)  # returns the exit code in unix
            print('Returned value:', returned_value)

            # Set done (for the day) to true if the page date == today
            # This stops unecessary retrieval of the page
            if page_date.date() == datetime.now().date(): done = True
        else:
            print('Gap in data')
            break
    else:
        print('Spreadsheet is up to date')
        if page_date.date() == datetime.now().date(): done = True

    # Check at time_between interval between 4 and 8 PM
    if tnow.hour >= start_checking and not done:
        print('{:%H:%M} No luck so far try again in {:.0f}, done = {}'
                .format(tnow, time_between/60, done))
        time.sleep(time_between)
    else:
        while tnow.hour < start_checking or done:
            print('{:%H:%M} Try again in {:.0f}, done = {}'
                    .format(tnow, time_between/60, done))
            time.sleep(time_between)
            tnow = datetime.now().time()
            if tnow.hour < start_checking: done = False
        #enwhile
    #endif

#endwhile
