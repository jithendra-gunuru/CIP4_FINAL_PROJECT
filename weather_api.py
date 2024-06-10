import requests

API_BASE_URL1 = "http://api.openweathermap.org/geo/1.0/direct?"
API_BASE_URL2 = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "a9664181096a9d07f0b38b2baf6ba7bd"
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
            print("run again and enter new city")
        
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
                print(temp + "  ==>  " + str(round(float(temperature[temp])-273.15, 2)) + "°C" )
            if temp == 'feels_likefeels_like':
                print(temp + "  ==>  " + str(round(float(temperature[temp])-273.15, 2)) + "°C" )
            if temp == 'temp_min':
                print(temp + "  ==>  " + str(round(float(temperature[temp])-273.15, 2)) + "°C" )
            if temp == 'temp_max':
                print(temp + "  ==>  " + str(round(float(temperature[temp])-273.15, 2)) + "°C" )
            if temp == 'pressure':
                print(temp + "  ==>  " + str(temperature[temp])+ " Hectopascal(hPa)")
            if temp == 'humidity':
                print(temp + "  ==>  " + str(temperature[temp]) + "%")
                print("Humidity refers to the amount of water vapor present in the air compared to the maximum amount of water vapor the air can hold at that specific temperature.")                                  
        print("visibility ==> " + str(weather_info["visibility"]) + 'm')
        print("wind ==> " + str(weather_info["wind"]))
def main():
    city_name = input("enter city name to display weather: ")
    co_ordinates = search_location(city_name)
    map_location = collect_co_ordinates(co_ordinates)
    weather_info = retrive_weather_info(map_location)
    display_format_weather_info(weather_info)

if __name__ == "__main__":
    main()

