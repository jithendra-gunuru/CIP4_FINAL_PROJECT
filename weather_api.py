import requests

API_BASE_URL1 = "http://api.openweathermap.org/geo/1.0/direct?"
API_BASE_URL2 = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "d4fef8354c4bea2b5e1eec3ee5dc0ec3"

def search_location(city_name):
    params ={
        "q" : city_name,
        "appid" : API_KEY
    }
    response_geo = requests.get(API_BASE_URL1, params)
    return response_geo.json()

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
        
def retrive_weather_info(map_location):
    if map_location:
        params = {
            "lat" : map_location["latitude"],
            "lon" : map_location["longitude"],
            "appid" : API_KEY
        }
        response_weather = requests.get(API_BASE_URL2, params)
        return response_weather.json()


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
def kelvin_to_celsius(temp):
    celsius = (temp)-273.15
    return celsius
def round_the_floats(celsius):
    celsius = round(celsius,2)
    return celsius
def main():
    city_name = input("enter city name to display weather(press enter to quit): ")
    while city_name != "":
        co_ordinates = search_location(city_name)
        map_location = collect_co_ordinates(co_ordinates)
        weather_info = retrive_weather_info(map_location)
        display_format_weather_info(weather_info)
        city_name = input("enter city name to display weather(press enter to quit): ")
        
    

if __name__ == "__main__":
    main()

