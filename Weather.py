import requests

city_name = "lahore"
API_key = 'ebd4f98c02b06252576d2a02d4c9d7a9'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Current Temrature Is ', data['main']['temp'])
    print('Feels Like Temrature Is ',  data['main']['feels_like'])
    print('General Weather Is',  data['weather'][0]['description'])
    print('Humidity Is ',  data['main']['humidity'])
    

    

     

   