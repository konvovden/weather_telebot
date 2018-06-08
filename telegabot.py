import main
import tgflow as tgf
from tgflow import TgFlow as tgf
from tgflow import handles as h
from enum import Enum
key='617530729:AAGS4jp0eHv5jAvIkvzbr5TGmTcriIqUzzw'

def sendLocation(i):    
    lat = i.latitude
    lon = i.longitude
    weatherMessage = main.GetWeatherMessage(lat, lon)
    tgf.bot.send_message(weatherMessage)

class States(Enum):
    START=1

UI = {
    States.START:
    {'t':'Это бот, который показывает погоду по геопозиции! Выберите нужную точку на карте, чтобы узнать там текущую погоду!',
        "react":h.action(sendLocation, react_to = 'location')}}

tgf.configure(token=key,
                 state=States.START,
                 data={"foo":'bar'})
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