import json
import urllib.request
import requests
from datetime import datetime
from dateutil import tz
from timezonefinder import TimezoneFinder

def get_IDs(link): # user_ID swarm, venue_ID foursquare
    try:
        my_request = urllib.request.urlopen(link)
        my_HTML = my_request.read().decode("utf8")
        ID_foursquare = my_HTML.split(' href=\"https://foursquare.com/v/')[1].split('/')[1].split('\"')[0]
        ID_swarm = my_HTML.split("https:\/\/fastly.4sqi.net\/img\/user\/")[1].split("\"id\":\"")[1].split("\"")[0]
        country = my_HTML.split('cc\":\"')[1].split("\"")[0]
        city = my_HTML.split("city\":\"")[1].split("\"")[0]
        categorie = my_HTML.split("categories\":")[1].split("name\":\"")[1].split("\"")[0]
        name = my_HTML.split(" | ")[1].split("<")[0]
        lon = my_HTML.split("latitude\" /><meta content=\"")[1].split("\"")[0]
        lat = my_HTML.split("longitude\" /><meta content=\"")[1].split("\"")[0]
        return ID_swarm, ID_foursquare, country, city, categorie, name, lon, lat
    except:
        return "0", "0", "0", "0", "0", "0", "0", "0"

def convert_tz(time, lat, lon):
    tf = TimezoneFinder(in_memory=True)
    loc = tf.timezone_at(lng=float(lon), lat=float(lat))
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz(loc)
    utc = datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    return central

def main():
    file = open("database.json", "r")
    file_print = open("data.csv", "w")
    print("fsq_id;swm_id;name;categorie;country;city;timestamp;lat;long", file=file_print)
    for json_file in file:
        try:
            json_file = json_file[0:len(json_file)-1]
            twt_id = json_file.split("\'id\': \'")[1].split("\'")[0] # tweet
            if "\'text\': \"" in json_file:
                text = json_file.split("\'text\': \"")[1].split("\"")[0]
            else:
                text = json_file.split("\'text\': \'")[1].split("\'")[0]
            if "https://t.co" not in json_file:
                continue
            elif "\\n" in json_file:
                link = text.split(" ")    
                link = link[len(link)-1].split("\\n")
            else:
                link = text.split(" ")
            link = link[len(link)-1]
            if "…" in link or "https://t.co" not in link:
                continue
            tmp = get_IDs(link)
            swm_id = tmp[0]
            fsq_id = tmp[1]
            loc = tmp[2]
            city = tmp[3]
            cat = tmp[4]
            name = tmp[5]
            lon = tmp[6]
            lat = tmp[7]
            time = convert_tz(json_file.split("\'timestamp\': \'")[1].split("\'")[0], lat, lon)
            if swm_id == '0':
                continue
            print(fsq_id + ";" + swm_id + ";" + name + ";" + cat + ";" + loc + ";" + city + ";" + str(time) + ";" + lat + ";" + lon, file=file_print)
        except:
            continue
        
if __name__ == "__main__":
    main()
