import googlemaps
import pprint
import time
import requests
import json

API_KEY = 'AIzaSyDE1bap6fzYKlWS9UahPmgxbhAIFQNIbz0'

NEARBY_SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

gmaps = googlemaps.Client(key=API_KEY)

places = []
#Might be useful later
'''
def search_places(place):
    places_list = gmaps.places_autocomplete(input_text=place)
    for place in places_list:
        places.append(place["description"])
    print(places)
'''

'''
def search(place):
    places = gmaps.find_place(input=place, input_type="textquery", fields='geometry')
    print(places)
'''

def search(place):
    url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=' + place + '&inputtype=textquery&fields=name,formatted_address&key=' + API_KEY
    #url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=' + API_KEY
    places = requests.get(url)
    json = places.json()
    print(json)
    formatted_address = json["candidates"][0]["formatted_address"]
    print(formatted_address)
    return formatted_address

g_hq_lat = gmaps.geocode('501 Twin Peaks Blvd, San Francisco, CA 94114')[0]["geometry"]["location"]["lat"]

g_hq_long = gmaps.geocode('501 Twin Peaks Blvd, San Francisco, CA 94114')[0]["geometry"]["location"]["lng"]

def get_lat_long(address):
    lat = gmaps.geocode(address)[0]["geometry"]["location"]["lat"]
    long = gmaps.geocode(address)[0]["geometry"]["location"]["lng"]
    return lat,long

def find_nearby(lat, long):
    json_result = gmaps.places_nearby(location=str(lat) + ', ' + str(long), radius=20000, type = "tourist_attraction, restaurant")
    array = []
    result = json_result["results"]
    for location in result:
        array.append(location["name"])
    print(array)

#find_nearby(g_hq_lat, g_hq_long)

address = search("lucalis")
lat, long = get_lat_long(address)
find_nearby(lat, long)
