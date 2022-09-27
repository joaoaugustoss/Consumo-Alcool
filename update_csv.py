import urllib.request

def get_html(link):
    try:
        my_request = urllib.request.urlopen(link)
        my_HTML = my_request.read().decode("utf8")
        lon = my_HTML.split("latitude\" /><meta content=\"")[1].split("\"")[0]
        lat = my_HTML.split("longitude\" /><meta content=\"")[1].split("\"")[0]
        return lat, lon
    except:
        return "0","0"

def main():
    try:
        file = open("data.csv", "r")
        file_print = open("new_data.csv", "a")
        print("twt_id,fsq_id,swm_id,link,name,categorie,country,state,city,timestamp,latitude,longitude", file=file_print)
        for f in file:
            if f.split(",")[9] == "link" or len(f.split(",")[6]) > 2 or "&" in f.split(",")[4]:
                continue
            r = get_html(f.split(",")[3])
            lat = r[0]
            lon = r[1]
            print(f.strip()+","+lat+","+lon, file=file_print)
    except:
        print("Main error")

if __name__ == "__main__":
    main()

