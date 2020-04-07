import os
import time
from datetime import datetime

from urllib.request import urlopen

cmd = "./run"
time_between = 30 * 60  #in seconds
url = "https://www.arcgis.com/sharing/rest/content/items/e5fd11150d274bebaaf8fe2a7a2bda11/data"

site = urlopen(url)
meta = site.info()
prev_mod = meta.get('Last-Modified')
while True:
    site = urlopen(url)
    meta = site.info()
    mod = meta.get('Last-Modified')
    print(datetime.now(), mod)
    if  mod != prev_mod:
        returned_value = os.system(cmd)  # returns the exit code in unix
        print('Returned value:', returned_value)
        prev_mod = mod
    time.sleep(time_between)
