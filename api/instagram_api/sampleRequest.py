import requests
from io import BytesIO
from PIL import Image

def getListOfPosts(location):
    end_cursor = ''
    page_count = 2
    all_posts = []
    post_url = ""
    max_like = 0
    for i in range(0, page_count):

        url = "https://www.instagram.com/explore/tags/{}/?__a=1&max_id={}".format(location, end_cursor)

        response = requests.get(url)
        data = response.json()
        end_cursor = data['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
        list_of_posts = (data['graphql']['hashtag']['edge_hashtag_to_media']['edges'])
        for post in list_of_posts:
            all_posts.append(post['node'])
    print("Finished getting posts")
    return all_posts

def getTopPost(location):
    end_cursor = ''
    page_count = 10
    post_url = ""
    max_like = 0
    for i in range(0, page_count):
        url = "https://www.instagram.com/explore/tags/{}/?__a=1&max_id={}".format(location, end_cursor)
        response = requests.get(url)
        data = response.json()
        end_cursor = data['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
        list_of_posts = (data['graphql']['hashtag']['edge_hashtag_to_media']['edges'])
        for post in list_of_posts:
            likes = post['node']['edge_media_preview_like']['count']
            if (likes > max_like):
                post_url = "https://www.instagram.com/p/{}/?__a=1".format(post['node']['shortcode'])
                max_like = likes
    print("Finished getting posts")
    print(post_url)
    return max_like

def getLocations(list_of_posts):
    locations = []
    count = 0
    dict = {}
    print("Extracting data from posts...")
    for post in list_of_posts:
        shortcode = post['shortcode']
        url = "https://www.instagram.com/p/{}/?__a=1".format(shortcode)
        response = requests.get(url)
        data = response.json()
        likes = data['graphql']['shortcode_media']['edge_media_preview_like']['count']
        dict[url] = likes
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
    sorted_dict = sorted(dict.items(), key= lambda x: x[1], reverse=True)
    for i in sorted_dict:
        print(i[0], i[1])
    print(locations)

def getTopPostFromList(list_of_posts):
    post_url = ""
    max_like = 0
    for post in list_of_posts:
        shortcode = post['shortcode']
        url = "https://www.instagram.com/p/{}/?__a=1".format(shortcode)
        response = requests.get(url)
        data = response.json()
        likes = data['graphql']['shortcode_media']['edge_media_preview_like']['count']
        if (likes > max_like):
            max_like = likes;
            post_url = url;
    return max_like

# all_posts = getListOfPosts("halfmoonbay")
print(getTopPost("halfmoonbay"))