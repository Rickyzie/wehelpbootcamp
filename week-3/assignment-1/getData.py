import requests
import csv
import pandas as pd
import json
from datetime import date
url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)
jsonObject = json.loads(response.text)["result"]["results"]
jsonDataFrame = pd.DataFrame(jsonObject, columns = jsonObject[0].keys())
jsonDataFrame['xpostDate'] = pd.to_datetime(jsonDataFrame['xpostDate']).dt.date
jsonDataFrame= jsonDataFrame.loc[jsonDataFrame['xpostDate']> date(2015, 1, 1)]
df=pd.concat(
    [jsonDataFrame["stitle"],
    jsonDataFrame["address"].str.extract(pat= '((?<=\s)..區)',expand=False),
    jsonDataFrame["longitude"],
    jsonDataFrame["latitude"],
    jsonDataFrame["file"].str.extract(pat= '(http.*?(jpg|JPG))',expand=False)]
    ,axis=1)
df.to_csv("taipeiDayTripResourse.csv",header=False, index=False)
