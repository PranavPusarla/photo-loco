import googlemaps
import pprint
import time
import requests
import json

API_KEY = 'AIzaSyDE1bap6fzYKlWS9UahPmgxbhAIFQNIbz0'

NEARBY_SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

gmaps = googlemaps.Client(key=API_KEY)

g_hq_lat = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')[0]["geometry"]["location"]["lat"]

g_hq_long = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')[0]["geometry"]["location"]["lng"]
'''
for place in result['results']:
    place_id = place['place_id']
    fields = ['name', 'formatted_phone_number', 'type']
    details = gmaps.place(place_id=place_id, fields=fields)
    print(details)
'''

def find_nearby(lat, long):
    json_result = gmaps.places_nearby(location=str(lat) + ', ' + str(long), radius=20000, type='tourist_attraction')
    array = []
    result = json_result["results"]
    for location in result:
        array.append(location["name"])
    print(array)

find_nearby(g_hq_lat, g_hq_long)