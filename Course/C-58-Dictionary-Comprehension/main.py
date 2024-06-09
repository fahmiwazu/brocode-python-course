########### Dictionary Comprehension in Python
## Converting value to new value in dictionary
cities_in_F = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
cities_in_C = {key: round((value-32)*(5/9)) for(key,value) in cities_in_F.items()}
print(cities_in_C)
## Selecting sunny weather from dictionary
weather = {'New York':"Snowing",'Boston':"Sunny",'Los Angeles':"Sunny",'Chicago':"Cloudy"}
sunny_weather = {key : value for (key,value) in weather.items() if value=="Sunny"}
print(sunny_weather)
## Selecting if/else in dictionary
cities = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
desc_cities = {key : ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
print(desc_cities)
## Replace if/else with function in dictionary
def check_suhu(value):
    if value >=70:
        return "HOT"
    elif 60 >= value >= 40:
        return "Warm"
    else:
        return "COLD"

cities = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
desc_cities = {key : check_suhu(value) for (key,value) in cities.items()}
print(desc_cities)