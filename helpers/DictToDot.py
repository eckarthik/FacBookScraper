class DotDict:
    """Class to convert a dictionary and to be able to refer the keys by dot"""

    def __init__(self,dictionary):
        self.items = dictionary

    def __getattr__(self, key):
        try:
            return self.items[key]
        except KeyError:
            raise AttributeError(key)