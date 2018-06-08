import requests
import json
import os
import sys

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



# http://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20180608T081728Z.5684da981c2a602d.7822398cfcda6dbcde646aa60813bcac2478b205&text=weather%20clear&lang=en-ru&format=plain

def GetWeatherMessage(lat, lon) -> str:
	response = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + weather_key)
	print(response.text + '\n')
	weather = json.loads(response.text)
	print(weather['coord'])

	response = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key='+yandex_translate_key+'&lang=eu-ru&text=weather%20' + weather['weather'][0]['main'])
	# weather_text = json.loads(response.text)
	# weather_text = weather_text['text']
	weather_text = json.loads(response.text)
	weather_text = str(weather_text['text'][0]).replace('погода', '').replace(' ', '')
	returned_string = ''

	returned_string += 'Географические координаты:\n'
	returned_string += 'Широта: ' + str(lat) + '. '
	returned_string += 'Долгота: ' + str(lon) + '.\n'
	returned_string += 'Погода: ' + weather_text + '\n'
	returned_string += 'Температура: ' + str(int(weather['main']['temp'] - 273)) + '°\n'
	returned_string += 'Давление: ' + str(int(weather['main']['pressure']*0.750062)) + 'мм. рт. ст (' + str(int(weather['main']['pressure'])) + ' гПа)\n'
	returned_string += 'Влажность: ' + str(int(weather['main']['humidity'])) + '%\n'
	returned_string += 'Скорость ветра: ' + str(weather['wind']['speed']) + ' м/с'
 
	return returned_string


