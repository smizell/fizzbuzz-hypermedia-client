from siren import SirenResource as Hyperclient

BASE_URL = "http://fizzbuzzaas.herokuapp.com"

def fizzbuzz(resource):
    """
    Prints the fizzbuzz value and follows "next" links
    """
    print resource.properties["value"]

    if resource.has_link("next"):
        fizzbuzz(resource.follow_link("next"))

def begin_fizzbuzz(resource):
    """
    Follows the first link, then hands off to fizzbuzz
    """
    if resource.has_link("first"):
        fizzbuzz(resource.follow_link("first"))

def custom_fizzbuzz(root_resource, params):
    """
    Submits actions for custom fizzbuzz
    """
    resource = root_resource.take_action("custom-fizzbuzz", params)
    begin_fizzbuzz(resource)

root_resource = Hyperclient(BASE_URL, path="/")
params = { "startsAt": 4, "endsAt": 20, "add": 2 }
custom_fizzbuzz(root_resource, params)
