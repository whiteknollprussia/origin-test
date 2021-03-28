#!/home/andrei/.pyenv/shims/python3
import datetime
import requests

url_api = 'https://api.openweathermap.org/data/2.5/onecall?'
lat = '51.672'
lon = '39.184'
exclude = 'week'
units = 'metric'
app_id = '36e61dee00a33dc60d14bc359230718c'
url = url_api + 'lat={}&lon={}&exclude={}&units={}&appid={}'.format(lat, lon, exclude, units, appid)


def daily_temp(url: str):
    try:
        response = requests.post(url)
        json_dat = response.json()
        now_time = datetime.datetime.fromtimestamp(json_dat['daily'][0]['dt'])
        delta = datetime.timedelta(days=5)
        format = '%d %b %Y'
        degree = str(u'\N{DEGREE SIGN}') + 'C'
        for dic in json_dat['daily']:
            value = datetime.datetime.fromtimestamp(dic['dt'])
            if value <= (delta + now_time):
                print(value.strftime(format))
                print('morning temperature:', dic['temp']['morn'], degree)
                print('maximum temperature:', dic['temp']['max'], degree)
    except:
        print('Something error')


daily_temp(url)
