import requests
api_key='9c3152d0f252658605e238d897e909c6'
user_input=input("Enter the city =>")
# print(user_input)
weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}")
# print(weather_data.status_code)
if(weather_data.status_code==200):
  data=weather_data.json()
  x=data['main']['temp']
  curr_temp=int(x-273.15)
  description=data['weather'][0]['description']
  print(f" current Temp of {user_input} is {curr_temp} and {description} ")
else:
  print("city is not Found")






