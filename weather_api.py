import requests

API_BASE_URL1 = "http://api.openweathermap.org/geo/1.0/direct?"
API_BASE_URL2 = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "fb049738ebccf16cb4ea2efbdf559f11"
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
        
def retrive_weather_info(map_location):
    params = {
          "lat" : map_location["latitude"],
          "lon" : map_location["longitude"],
          "appid" : API_KEY
     }
    response_weather = requests.get(API_BASE_URL2, params)
    return response_weather.json()


def display_format_weather_info(weather_info):
     print("weather_report: ", weather_info["weather"][0]['main'])
     print("weather_report description: ", weather_info["weather"][0]['description'])
     
            

def main():
    city_name = input("enter city name to display weather: ")
    co_ordinates = search_location(city_name)
    map_location = collect_co_ordinates(co_ordinates)
    weather_info = retrive_weather_info(map_location)
    display_format_weather_info(weather_info)

if __name__ == "__main__":
    main()