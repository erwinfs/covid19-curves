import wget
import os

filePath = 'DailyConfirmedCases.xlsx'
url = "https://www.arcgis.com/sharing/rest/content/items/e5fd11150d274bebaaf8fe2a7a2bda11/data"

if os.path.exists(filePath):
    os.remove(filePath)

wget.download(url, filePath)
