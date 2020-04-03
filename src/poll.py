import os
import time
from datetime import datetime

from urllib.request import urlopen

cmd = "./run"
timeBetween = 30 * 60  #in seconds
url = "https://www.arcgis.com/sharing/rest/content/items/e5fd11150d274bebaaf8fe2a7a2bda11/data"

site = urlopen(url)
meta = site.info()
prevMod = meta.get('Last-Modified')
while True:
    site = urlopen(url)
    meta = site.info()
    mod = meta.get('Last-Modified')
    print(datetime.now(), mod)
    if  mod != prevMod:
        returned_value = os.system(cmd)  # returns the exit code in unix
        print('Returned value:', returned_value)
        prevMod = mod
    time.sleep(timeBetween)
