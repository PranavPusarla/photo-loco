import requests
from io import BytesIO
from PIL import Image

def get_list_of_posts(location):

    end_cursor = ''
    page_count = 2
    all_posts = []
    for i in range(0, page_count):

        url = "https://www.instagram.com/explore/tags/{}/?__a=1&max_id={}".format(location, end_cursor)

        response = requests.get(url)
        data = response.json()
        end_cursor = data['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
        list_of_posts = (data['graphql']['hashtag']['edge_hashtag_to_media']['edges'])
        for post in list_of_posts:
            all_posts.append(post['node'])
    return all_posts

def get_locations(list_of_posts):
    locations = []
    count = 0;
    for post in list_of_posts:
        shortcode = post['shortcode']
        url = "https://www.instagram.com/p/{}/?__a=1".format(shortcode)
        print(url)
        response = requests.get(url)
        data = response.json()
        try:
            location = data['graphql']['shortcode_media']['location']['name']
            locations.append({"shortcode": shortcode, "location": location})
        except:
            data['graphql']['shortcode_media']['location']='None'

        image_url = data['graphql']['shortcode_media']['display_url']

        #just shows first 5 pictures
        if(count < 5):
            image_response = requests.get(image_url)
            img = Image.open(BytesIO(image_response.content))
            img.show()
        count +=1

    print(locations)

all_posts = get_list_of_posts("russia")
get_locations(all_posts)