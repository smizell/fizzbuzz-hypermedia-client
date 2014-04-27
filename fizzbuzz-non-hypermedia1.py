import requests

BASE_URL = "http://fizzbuzzaas.herokuapp.com"

def fizzbuzz(params):
    url = BASE_URL + "/fizzbuzz"
    response = requests.get(url, params=params)
    response_json = response.json()
    return response_json["properties"]["value"]

for number in range(1, 101):
    print fizzbuzz({"number": number })
