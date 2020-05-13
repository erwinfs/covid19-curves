import os
import time
import pandas as pd
from datetime import datetime
from datetime import timedelta
from lxml import html
import requests
from urllib.request import urlopen

cmd = "./run"
time_between = 1 * 60  # in seconds
start_checking = 9 # hour of day after which the script will check for new data
data_input_fname = "./data/DailyConfirmedCases.xlsx"
url = 'https://www.gov.uk/guidance/coronavirus-covid-19-information-for-the-public'

done = False
while True:
    tnow = datetime.now().time()
    print('Taking a look at {}:{}'.format(tnow.hour, tnow.minute))

    # Read spread sheet data
    ss = pd.read_excel(data_input_fname)
    ss_last = ss.iloc[-1] # Last row
    last_date = ss_last['DateVal']

    # Retrieve website
    page = str(requests.get(url).content)
    df = pd.read_html(page)

    # Read news deaths and Pillar 1 positive tests
    new_deaths = df[0]['Deaths in all settings'][0]
    new_cases = df[1]['Pillar 1'][2]

    # Find date of data
    date_str = page.partition('Number of cases and deaths')[2]
    date_str = date_str.partition('As of')[2]
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
            if page_date.date() == datetime.now().date() : done = True
        else:
            print('Gap in data')
            break
    else:
        print('Spreadsheet is up to date')
        # done = True

    # Check at time_between interval between 4 and 8 PM
    h_now = datetime.now().time().hour
    m_now = datetime.now().time().minute
    if h_now >= start_checking and not done:
        print('It is {}:{} no luck so far try again in {:.0f} minutes, done = {}'
                .format(h_now, m_now,time_between/60, done))
        time.sleep(time_between)
    else:
        while h_now < start_checking or done:
            print('It is {}:{} try again in {:.0f} minutes, done for the day {}'
                    .format(h_now, m_now, time_between/60, done))
            time.sleep(time_between)
            h_now = datetime.now().time().hour
            m_now = datetime.now().time().minute
            if h_now < start_checking: done = False
        #enwhile
    #endif

#endwhile
