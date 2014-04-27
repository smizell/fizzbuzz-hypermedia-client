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

root_resource = Hyperclient(BASE_URL, path="/")
begin_fizzbuzz(root_resource)
