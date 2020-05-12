import os
import time
import pandas as pd
from datetime import datetime
from datetime import timedelta
from lxml import html
import requests
from urllib.request import urlopen

cmd = "./run"
time_between = 15 * 60  # in seconds
data_input_fname = "./data/DailyConfirmedCases.xlsx"
url = 'https://www.gov.uk/guidance/coronavirus-covid-19-information-for-the-public'


# Read spread sheet data
ss = pd.read_excel(data_input_fname)
ss_last = ss.iloc[-1] # Last row
last_date = ss_last['DateVal']

while True:
    tnow = datetime.now().time()
    print('Taking a look at {}:{}'.format(tnow.hour, tnow.minute))
    # Retrieve website
    page = str(requests.get(url).content)
    df = pd.read_html(page)

    # Read news deaths and Pillar 1 positive tests
    new_deaths = df[0]['Deaths in all settings'][0]
    new_cases = df[1]['Pillar 1'][2]

    # Find date of data
    date_str = page.partition('As of')[2]
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
        else:
            print('Gap in data')
            break
    else:
        print('Spreadsheet is up to date')

    # Check at time_between interval between 4 and 8 PM
    h_now = datetime.now().time().hour
    if h_now in range (16, 21):
        print('It is between 16:00 and 20:00 try again in {:0} minutes'
                .format(time_between/60))
        time.sleep(time_between)
    else:
        print('It is not between 16:00 and 20:00 try again in {:0} minutes'
                .format(time_between/60))
        while h_now not in range(16,21):
             time.sleep(time_between)
             h_now = datetime.now().time().hour
        #enwhile
    #endif

#endwhile
