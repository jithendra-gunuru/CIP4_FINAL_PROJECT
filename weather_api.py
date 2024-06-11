"""
python version : Python 3.12.4
python requests version : Version: 2.32.3
aim of the program: This python program aims to print relative co-ordinates and weather report of the any available city in used API 
                    data of user choice.
functionality: This program takes city name as string continously to output it's relative co-ordinates and weather report until user
               enters empty string.
"""

#importing python requests library for api calls
import requests

#api url to get relative co-ordinates (latitude, longitude)
API_BASE_URL1 = "http://api.openweathermap.org/geo/1.0/direct?"

#api url to get weather details for given relative co-ordinates (latitude, longitude)
API_BASE_URL2 = "https://api.openweathermap.org/data/2.5/weather?"

#api key to combine with above urls to give input for request.get(url, api_key)
API_KEY = ""      

"""
below function takes city_name as function parameter and creates dictionary called params which include keys i.e q for city name, appid
for api key. after creating dictionary it will call api with two arguments (API_BASE_URL1, params) and it stores api response in 
response_geo variable and returns response_geo in json format
"""
def search_location(city_name):
    params ={
        "q" : city_name, 
        "appid" : API_KEY
    }
    response_geo = requests.get(API_BASE_URL1, params)
    return response_geo.json()

"""
below function takes co_ordinates as function parameter and checks whether it contains relative co_ordinates json data or not, if it 
contain json data, it will excute if block and filter for relative co-ordinates(latitude and longtitude) and city name and saves it in
location dictionary and also prints city name , and relative co-ordinates (latitude and longitude) and last portion of the if block 
returns location dictionary. if the function parameter i.e co_ordinates doesn't contain co-ordinates then the function will excutes
else block.
"""
def collect_co_ordinates(co_ordinates):
        if co_ordinates: 
            city_name =co_ordinates[0]["name"]
            lat = co_ordinates[0]["lat"]
            lon = co_ordinates[0]["lon"]
            print("city_name =", city_name, ", latitude = ",lat,", longitude = ", lon)
            location = {}
            location["latitude"] = lat
            location["longitude"] = lon
            return location
        else:
            print("we do not have this city weather report")
            print("enter new city agian in the next coming prompt")

"""
below function takes map_location as function parameter and checks if map_location is null or not. if map_location is not null
then create params dictionary and takes values from map_location for keys(lat, lon) and for key appid it takes value from 
global variable API_KEY, after that it will make a api call by passing arguments(API_BASE_URL2, params) then stores api response
(i.e weather report) in response_weather varibale and next returns api response i.e response_weather in json format.
"""      
def retrive_weather_info(map_location):
    if map_location:
        params = {
            "lat" : map_location["latitude"],
            "lon" : map_location["longitude"],
            "appid" : API_KEY
        }
        response_weather = requests.get(API_BASE_URL2, params)
        return response_weather.json()
    
"""
below function takes weather_info as function parameter and checks if weather_info is null or not, if not null, excutes if block.
in if block, it first prints weather_report, weather_report description, then prints dictionary contains main weather details
like tempature, feels a like temp, min_temp, max_temp, pressure and humidity. then for loop loop's over dictionary keys and for 
temperature related keys, it verifies with if condition and it converts the temp values kelvin to celsius by calling 
kelvin_to_celsius(temperature['temp']) function and stores it in variable after that it updates the variable by calling 
round_the_floats(celsius) function. after that for key = pressure and key = humidity it prints with suitable string text which 
contains respective key value from dictionary respective to their units i.e hpa and % from here for loop ends. after next 3 print 
statements print's visibility, wind details in dictionary, timezone values with their units extracted from function parameter 
weather_info. 
"""
def display_format_weather_info(weather_info):
    if weather_info:
        print("weather_report: ", weather_info["weather"][0]['main'])
        print("weather_report description: ", weather_info["weather"][0]['description'])
        print(weather_info["main"])
        temperature = weather_info["main"]
        for temp in temperature:
            if temp == 'temp':
                celsius1 = kelvin_to_celsius(temperature['temp'])
                celsius1 = round_the_floats(celsius1)
                print(temp + "  ==>  " + str(celsius1) + "°C" ) 
            if temp == 'feels_like':
                celsius2 = kelvin_to_celsius(temperature['feels_like'])
                celsius2 = round_the_floats(celsius2)
                print(temp + "  ==>  " + str(celsius2) + "°C" ) 
            if temp == 'temp_min':
                celsius3 = kelvin_to_celsius(temperature['temp_min'])
                celsius3 = round_the_floats(celsius3)
                print(temp + "  ==>  " + str(celsius3) + "°C" )
            if temp == 'temp_max':
                celsius4 = kelvin_to_celsius(temperature['temp_max'])
                celsius4 = round_the_floats(celsius4)
                print(temp + "  ==>  " + str(celsius4) + "°C" )
            if temp == 'pressure':
                print(temp + "  ==>  " + str(temperature[temp])+ " Hectopascal(hPa)")
            if temp == 'humidity':
                print(temp + "  ==>  " + str(temperature[temp]) + "%")
                print("Humidity refers to the amount of water vapor present in the air compared to the maximum amount of water vapor the air can hold at that specific temperature.")                                  
        print("visibility ==> " + str(weather_info["visibility"])+ "m")
        print("wind ==> " + str(weather_info["wind"]))
        print("time_zone ==> " + str(weather_info["timezone"]) + " seconds")

"""
below function takes temp(temperature in kelvin) as function parameter and converts it to celsius and return the celsius value
"""
def kelvin_to_celsius(temp):
    celsius = (temp)-273.15
    return celsius

"""
below function takes celsius value as function parameter and rounds the float value to 2 digits after floating point.
"""
def round_the_floats(celsius):
    celsius = round(celsius,2)
    return celsius

"""
below function is main function AKA heart of this program, excution starts from here, it asks user to enter city 
and enter's while loop if user input is not null and call's search_location(city_name) function and stores it's return value 
in co_ordinates, then call's collect_co_ordinates(co_ordinates) function and stores it return value in map_location. then call's
retrive_weather_info(map_location) function and stores it return value in weather_info and then call's 
display_format_weather_info(weather_info) which displays weather and again asks city name to check while condition.
this process repeats until user enters null by pressing enter key in keyboard which ends while loop and program as well.
"""
def main():
    city_name = input("enter city name to display weather(press enter to quit): ")
    while city_name != "":
        co_ordinates = search_location(city_name)
        map_location = collect_co_ordinates(co_ordinates)
        weather_info = retrive_weather_info(map_location)
        display_format_weather_info(weather_info)
        city_name = input("enter city name to display weather(press enter to quit): ")
        

  
#below code searches for main function and tells python to start excution from there
if __name__ == "__main__":
    main()

