import requests

BASE_URL = "http://fizzbuzzaas.herokuapp.com"
STARTS_AT = 4
ENDS_AT = 20
ADD = 2

def fizzbuzz(resource):
    print resource["properties"]["value"]

    if "entities" in resource:
        fizzbuzz(resource["entities"][0])

def get_embedded_fizzbuzz(params):
    params["embed"] = True
    url = BASE_URL + "/fizzbuzz"
    response = requests.get(url, params=params)
    response_json = response.json()

    fizzbuzz(response_json["entities"][0])

get_embedded_fizzbuzz({"number": STARTS_AT, "endsAt": ENDS_AT,
                       "add": ADD, "firstNumber": 4})
