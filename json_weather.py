import json, requests, sys

# read location from command line
if(len(sys.argv)<2):
    print("Usgae : print the weather data")
    sys.exit()
location = " ".join(sys.argv[1:])


#download json data from openweathermap.org's website
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# load json data into python variable and print weather
weather_data = json.loads(response.text)

w =weather_data['list']

print('Current weather in {}:' .format(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
