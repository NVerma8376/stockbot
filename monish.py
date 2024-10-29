import requests
import alpha_vantage
import json


API_URL = "https://www.alphavantage.co/query" 
symbols = ['TCS']

for symbol in symbols:
        data = { "function": "TIME_SERIES_INTRADAY", 
        "symbol": symbol,
        "interval" : "60min",       
        "datatype": "json", 
        "apikey": "1I1QYECE05PE3PA7" } 
        response = requests.get(API_URL, data) 
        data = response.json()
        print(symbol)
        a = (data['Time Series (60min)'])
        keys = (a.keys())
        for key in keys:
                print(a[key]['2. high'] + " " + a[key]['5. volume'])