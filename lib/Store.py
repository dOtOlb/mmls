import sys
import datetime
import operator

class Store:
    """An implementation of the data store"""
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    __add = add
