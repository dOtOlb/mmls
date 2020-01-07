import sys
import datetime
import operator

class Store:
    """
    An implementation of the data store
    TO DO: need to add some more common supporting methods to the data store
    """
    def __init__(self):
        self.data = []

    # add method
    def add(self, item):
        self.data.append(item)

    __add = add
