import requests

class SirenBase:

    def _get_url(self, url, params={}):
        """
        Wraps requests get method
        """
        print "Following url %s" % url
        return requests.get(url, params=params)

    def _full_url(self, path):
        """
        Builds a full url from the base url and path
        """
        return self.base_url + path

    def to_json(self):
        """
        Returns json of response
        """
        return self.response_json

    def has_properties(self):
        return "properties" in self.response_json

    @property
    def properties(self):
        """
        Returns the properties, if there are any
        """
        if self.has_properties():
            return self.response_json["properties"]
        return None

    def has_links(self):
        """
        Boolean to tell if the response has links
        """
        return "links" in self.response_json

    @property
    def links(self):
        """
        Returns links in response, if there are any
        """
        if self.has_links():
            return self.response_json["links"]
        return None

    def has_link(self, link_rel):
        """
        Boolean to tell if response has a link relation
        """
        # See if the link relation is in the links
        if self.has_links():
            for link in self.links:
                if link_rel in link["rel"]:
                    return True

        # See if the link relation is embedded
        if self.has_embedded(link_rel):
            return True

        # Link relation wasn't found
        return False

    def follow_link(self, link_rel, params={}):
        """
        Follow a link to a new resource or return embedded
        """
        # If the resource is embedded, use that
        if self.has_embedded(link_rel):
            return SirenEmbedded(self.embedded(link_rel))

        # If the resource is linked, return a new resource
        for link in self.links:
            if link_rel in link["rel"]:
                return SirenResource(self.base_url, link["href"], params=params)

        # Nothing was found
        return None

    def has_embedded(self, link_rel):
        if "entities" in self.response_json:
            print "test"
            for entity in self.response_json["entities"]:
                if link_rel in entity["rel"]:
                    return True
        return False

    def embedded(self, link_rel):
        for entity in self.response_json["entities"]:
            if link_rel in entity["rel"]:
                return entity
        return None

    def has_actions(self):
        """
        Boolean to tell if response has actions
        """
        return "actions" in self.response_json

    def has_action(self, action_name):
        """
        Boolean to tell if response has a particular action name
        """
        if has_actions():
            for action in self.actions:
                if action["name"] == action_name:
                    return True
        return False

    @property
    def actions(self):
        """
        Returns all actions in the response
        """
        if self.has_actions():
            return self.response_json["actions"]
        return None

    def _get_action(self, action_name):
        """
        Returns the action matching the action name
        """
        for action in self.actions:
            if action["name"] == action_name:
                return action
        return None

    def take_action(self, action_name, params={}):
        """
        Submits the action with the given params
        """
        action = self._get_action(action_name)

        # Only GET support at the moment
        if action["method"] == "GET":
            return SirenResource(self.base_url, action["href"], params)

class SirenResource(SirenBase):
    """
    Class for a Siren resource
    """

    def __init__(self, base_url, path, params={}):
        self.base_url = base_url
        self.path = path
        self.params = params
        self.url = self._full_url(path)
        self.response = self._get_url(self.url, params)
        self.response_json = self.response.json()

class SirenEmbedded(SirenBase):
    """
    Class for handling embedded resources
    """

    def __init__(self, response_json):
        self.response_json = response_json
