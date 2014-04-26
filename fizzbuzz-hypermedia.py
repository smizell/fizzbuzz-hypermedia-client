from siren import SirenResource as Hyperclient

BASE_URL = "http://127.0.0.1:3000"

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

if __name__ == '__main__':
    # Get the root resource from the API
    root_resource = Hyperclient(BASE_URL, path="/", params={"embed": 1})

    # Start from the beginning
    #begin_fizzbuzz(root_resource)

    # Use a custom fizzbuzz
    params = { "embed": 1 }
    custom_fizzbuzz(root_resource, params)
