import requests

BASE_URL = "http://fizzbuzzaas.herokuapp.com"
STARTS_AT = 4
ENDS_AT = 20
ADD = 2

def fizzbuzz(params):
    url = BASE_URL + "/fizzbuzz"
    response = requests.get(url, params=params)
    response_json = response.json()
    print response_json["properties"]["value"]

    params["number"] += ADD

    if params["number"] <= ENDS_AT:
        fizzbuzz(params)

fizzbuzz({"number": STARTS_AT, "firstNumber": 4})
