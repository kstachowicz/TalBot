import json
import urllib
import sys

WEATHER_URL = "http://api.openweathermap.org/data/2.5/find?q=%s&units=metric&mode=json"

def get_weather(city_name):
    url = WEATHER_URL % city_name
    print "argument: ", city_name
    try:
        data = json.load(urllib.urlopen(url))
    except:
        return None

    try:
        item = data['list'][0]
        print 'Ok, here you have weather for %s:' % item['name']
        print 'Curret temperature is %s Celcius' % item['main']['temp']
        print 'You can expect %s.' % item['weather'][0]['description']
        print 'Temprature is between {0} and {1} Celcius'.format(item['main']['temp_min'], item['main']['temp_max']) 
        print 'The speed of wind is %s km/h' % item['wind']['speed']
    except:
        print "Sorry, but I don't understand. Whad do you want me to do?"
        return None

    try:
        rain = item['rain']['3h']
        if rain == 0:
            print "Its doesn't seem like raining in the nearest 3h"
        else:
            print "It might raining, about %s cm" % rain
    except:
        return None


if __name__ == "__main__":
    get_weather(sys.argv[1:])


