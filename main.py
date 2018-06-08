import requests
import json

weather_key = 'b23a723ded22b73ca842f89940aac7d0'
telegram_key = '617530729:AAGS4jp0eHv5jAvIkvzbr5TGmTcriIqUzzw'


# http://api.openweathermap.org/data/2.5/weather?lat=4&lon=139&appid=b23a723ded22b73ca842f89940aac7d0

def GetWeatherMessage(lat, lon) -> str:
	response = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + weather_key)
	print(response.text + '\n')
	weather = json.loads(response.text)
	print(weather['coord'])

	returned_string = ''

	returned_string += 'Географические координаты:\n'
	returned_string += 'Широта: ' + str(lat) + '. '
	returned_string += 'Долгота: ' + str(lon) + '.\nn'
	returned_string += 'Погода: ' + str(weather['weather'][0]['main'])
	return returned_string



