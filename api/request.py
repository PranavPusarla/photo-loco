from maps_request import place_textsearch, get_lat_long, find_nearby
from insta_request import get_list_of_posts, get_locations

place_set = place_textsearch("lucalis pizza")
first_place_in_search = place_set[0]
lat, long = get_lat_long(first_place_in_search["address"])
print(lat, long)

nearby = find_nearby(lat, long)
print(nearby)

first_nearby = nearby[0]
first_nearby = str(first_nearby.replace(" ", ""))

print(first_nearby)
posts = get_list_of_posts(first_nearby)
get_locations(posts)
