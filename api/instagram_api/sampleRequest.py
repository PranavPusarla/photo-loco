import requests

url = "https://www.instagram.com/explore/tags/italy/?__a=1"

response = requests.get(url)
data = response.json()

print(response)
print(data)