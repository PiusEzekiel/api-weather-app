import requests

from datetime import datetime

#my api key
user_api = '10dffcc5f7dbf88275d07bfdbc95365a'


while True:
	location = input("Enter the city name (or 'exit' to quit): ")
	
	if location.lower() == 'exit':
		break
		
	complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
	api_link = requests.get(complete_api_link)
	api_data = api_link.json()
	
	
	if api_data['cod'] == '404':
		print("This city, {} , is invalid, please check your city name".format(location))
		
	else:
		#these variables store and display data
		temp_city = ((api_data['main']['temp']) - 273.15)
		weather_desc = api_data['weather'][0]['description']
		hmdt = api_data['main']['humidity']
		wind_spd = api_data['wind']['speed']
		date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
		
		print ("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
		print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
		print ("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
		
		print ("Current temperature is: {:.2f} deg C".format(temp_city))
		print ("Current weather desc  :",weather_desc)
		print ("Current Humidity      :",hmdt, '%')
		print ("Current wind speed    :",wind_spd ,'kmph')

