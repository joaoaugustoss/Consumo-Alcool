import urllib.request
from datetime import datetime
from dateutil import tz
from timezonefinder import TimezoneFinder

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
    file = open("CP.csv", "r")
    file_print = open("updated.csv", "a")
    #print("fsq_id;swm_id;name;categorie;country;city;timestamp;latitude;longitude", file = file_print)
    for f in file:
        try:
            count = 0
            for i in f:
                if i == ",":
                    count += 1
            if f.split(',')[4].split(',')[0]== '0' or 'name'in f:
                continue
            fsq_id  = f.split(',')[ 1].split(',')[0]
            swm_id  = f.split(',')[ 2].split(',')[0]
            name    = f.split(',')[ 4].split(',')[0]
            cat     = f.split(',')[ 5].split(',')[0]
            country = f.split(',')[ 6].split(',')[0]
            city    = f.split(',')[ 8].split(',')[0]
            lat     = f.split(',')[10].split(',')[0]
            lon     = f.split(',')[11].split(',')[0]
            time    = convert_tz(f.split(',')[9].split(',')[0], lat, lon)
            print(str(fsq_id + ";" + swm_id + ";" + name + ";" + cat + ";" + country + ";" + city + ";" + str(time) + ";" + lat + ";" + lon).strip()) 
            print(str(fsq_id + ";" + swm_id + ";" + name + ";" + cat + ";" + country + ";" + city + ";" + str(time) + ";" + lat + ";" + lon).strip(), file = file_print) 
        except:
            print("erro")
            print("0,0,0,0,0,0,0,0,0",file=file_print)
            continue

    file.close(); file_print.close()
if __name__ == "__main__":
    main()

