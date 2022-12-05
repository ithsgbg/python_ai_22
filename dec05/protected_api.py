import requests

import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.geoapify.com/v1/geocode/search?text=Ljungsbergsgatan%2011%2C%20662%2036%20%C3%85m%C3%A5l%2C%20Sweden&apiKey=90201ce767c74f37852cbffd33b4c825"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

resp = requests.get(url, headers=headers)

print(resp.status_code)
data = resp.json()

print()

