import main
import tgflow as tgf
from tgflow import TgFlow as tgf
from tgflow import handles as h
from enum import Enum
key='617530729:AAGS4jp0eHv5jAvIkvzbr5TGmTcriIqUzzw'

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

tgf.configure(token=key,
                 state=States.START)
tgf.start(UI)

"""
from tgflow import TgFlow
from enum import Enum
key='539066078:AAHCUsr8ZoP9JtP5KqOMuL7f_UoFyyH6wik'
class States(Enum):
    START=1
TgFlow.configure(token=key,
                 state=States.START,
                 data={"foo":'bar'})
TgFlow.start({States.START:{'t':'hello'}})
"""