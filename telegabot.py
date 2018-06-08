import os
import sys
import main
import tgflow as tgf
from tgflow import TgFlow as tgf
from tgflow import handles as h
from enum import Enum

if os.path.isfile('keys.txt'):
    file = open('keys.txt', 'r')
    file = file.read()
    file.split('\n')
    weather_key = file[0]
    telegram_key = file[1]
    yandex_translate_key = file[2]
    print('API Keys успешно загружены!') 
else:
    print('Ошибка! Файл с API Keys не найден!')
    sys.exit()

def sendLocation(i): 
    print(i.location)
    lat = i.location.latitude
    lon = i.location.longitude
    weatherMessage = main.GetWeatherMessage(lat, lon)
    print(weatherMessage)
    tgf.bot.send_message(i.chat.id, weatherMessage)
    return States.WEATHER

class States(Enum):
    START=1,
    WEATHER=2

UI = {
    States.START:
    {'t':'Это бот, который показывает погоду по геопозиции! Выберите нужную точку на карте, чтобы узнать там текущую погоду!',
        "react":h.action(sendLocation, react_to = 'location')},
    States.WEATHER:
    {"react":h.action(sendLocation, react_to = 'location')}}

tgf.configure(token=telegram_key,
                 state=States.START)
tgf.start(UI)

"""
from tgflow import TgFlow
from enum import Enum
telegram_key='539066078:AAHCUsr8ZoP9JtP5KqOMuL7f_UoFyyH6wik'
class States(Enum):
    START=1
TgFlow.configure(token=telegram_key,
                 state=States.START,
                 data={"foo":'bar'})
TgFlow.start({States.START:{'t':'hello'}})
"""