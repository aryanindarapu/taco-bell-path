import requests
import csv
import json
import pprint
from bs4 import BeautifulSoup


URL_BASE = "http://locations.tacobell.com/"



def get_coords(locationHTML, locationCoordinateDict, nearbyCoordinatesDict):
    addressCoordinatePair = []
    curr = ""
    nearby = []
    first = True
    soup = BeautifulSoup(locationHTML, features="html.parser")
    for data in soup.find_all('script', {'class' : 'js-map-config'}):
        loaded = json.loads(data.text)
        try:
            coord = loaded['entities'][0]['profile']['yextDisplayCoordinate']
            if first:
                curr = str(str(coord['lat']) + ';' + str(coord['long']))
                address = soup.find('meta', {'itemprop' : 'streetAddress'}).get('content')
                locationCoordinateDict[curr] = address
            else:
                nearby.append(str(str(coord['lat']) + ';' + str(coord['long'])))
            first = False
        except:
            addresses = list(locationCoordinateDict.keys())
            if (len(addresses)) > 0:
                print (addresses[-1])
       
    nearbyCoordinatesDict[curr] = nearby

def get_nearest_coords(locationHTML):
    soup = BeautifulSoup(locationHTML, features="html.parser")
    for meta in soup.find_all('span'):
        if (meta.get('name') == "geo.position"):
            return meta.get('content')

def write_to_csv(file, locations):
    file = open(file, 'w')
    # writer = csv.writer(file)
    for location in locations:
        if location is None:
            continue
        file.write(location)
        file.write('\n')
    file.close()


def get_locations(data):
    # initial locations
    list_items = data.split("li>")
    locations = []
    for item in list_items:
        try:
            second = item.split("href=\"")[1]
            result = second.split("\"")[0]
            locations.append(result)
        except:
            print()

    # hidden locations
    extra_locations = []
    for location in locations.copy():
        data = requests.get(URL_BASE + location).text
        if "geo.position" not in data:
            locations.remove(location)
            # find hyperlinks to those locations
            soup = BeautifulSoup(data, features="html.parser")
            for a in soup.find_all('a', attrs={'class', 'Teaser-viewPage'}):
                link = a.get('href')
                modifiedLink = link.replace('.', '', 2).replace('/', '', 1)
                extra_locations.append(modifiedLink)
            

    locations += extra_locations
    return locations


def write_to_csv_new(locationCoordinateDict, nearbyCoordinatesDict):
    keys = list(locationCoordinateDict.keys())
    file = open("/Users/ashwinjain/Development/Final Project/data/final.csv", 'w')
    for i in range(len(keys)):
        currCoord = keys[i]
        file.write(locationCoordinateDict[currCoord])
        file.write(',')
        file.write(currCoord)
        for nearbyCoord in nearbyCoordinatesDict[currCoord]:
            file.write(','+ str(nearbyCoord))
        file.write('\n')
    file.close()
