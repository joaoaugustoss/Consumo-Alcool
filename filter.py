import json
import urllib.request
import requests

def get_IDs(link): # user_ID swarm, venue_ID foursquare
    try:
        my_request = urllib.request.urlopen(link)
        my_HTML = my_request.read().decode("utf8")
        ID_foursquare = my_HTML.split('href=\"https://foursquare.com/v/')[1].split('/')[1].split('\"')[0]
        ID_swarm = my_HTML.split("https:\/\/fastly.4sqi.net\/img\/user\/")[1].split("\"id\":\"")[1].split("\"")[0]
        return ID_swarm, ID_foursquare
    except:
        return "0", "0"

def fsq_api(fsq_id):
    try:
        url = "https://api.foursquare.com/v3/places/" + fsq_id
        headers = {
            "Accept": "application/json",
            "Authorization": "API_KEY"
        }
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        cat = data["categories"][0]['name']
        country = data["location"]['country']
        city = data["location"]['locality']
        state = data["location"]['region']
        name = data["name"]
        return cat, country, city, state, name
    except:
        return "0", "0", "0", "0", "0"

def main():
    file = open("database.json", "r")
    file_print = open("data.csv", "w")
    print("twt_id,fsq_id,swm_id,link,name,categorie,country,state,city,timestamp", file=file_print)
    for json_file in file:
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
        time = json_file.split("\'timestamp\': \'")[1].split("\'")[0]
        tmp = get_IDs(link)
        swm_id = tmp[0]
        fsq_id = tmp[1]
        fsq = fsq_api(fsq_id)
        cat = fsq[0]
        loc = fsq[1]
        city = fsq[2]
        state = fsq[3]
        name = fsq[4]
        print(twt_id + "," + fsq_id + "," + swm_id + "," + link + "," + name + "," + cat + "," + loc + "," + state + "," + city + "," + time, file=file_print)

if __name__ == "__main__":
    main()
