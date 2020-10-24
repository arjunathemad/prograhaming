#! python3
#fishing.py - get next five day fishing report from Accuweather
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta


# ////////////////// Get request for Accuweather URL \\\\\\\\\\\\\\\\\\\\\
#    header used to create User Agent to bypass 403 status code. User Agent Found in Network Developer Tools in Chrome.
header = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'}
#    URL for accuweather fishing report
url ='https://www.accuweather.com/en/us/mckinney/75069/fishing-weather/335923'
#    get url request and using header to produce 200 status code
result = requests.get(url,headers=header)


# //////////// Format 5 consecutive days \\\\\\\\\\\\

def five_day():
    start = datetime.now()
    end = start + timedelta(days=5)
    tmp = start
    dates = []

    while tmp < end:
        dates.append(tmp)
        tmp = tmp + timedelta(days=1)
    return dates

# /////////////// Get Fishing Report /////////////////////

def fishing_report():
    soup = BeautifulSoup(result.content, 'lxml')
    find_class = soup.find_all('div', class_='cond')
    conditions = []

    for i in find_class[:5]:
        for j in i:
            conditions.append(j.strip())
    return conditions


print('Per the Accuweather fishing report, the fishing forecast for the next 5 days is as follows:', end='\n\n')

for date, condition in zip(five_day(), fishing_report()):
    print(f'{date} ---- {condition}', end='\n')










