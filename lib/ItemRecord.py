import sys
import datetime
import operator

class ItemRecord:
    """A data structure holding all the information about an item"""
    def __init__(self, type, id, score, data):
        self.type = type
        self.id = id
        self.score = score
        self.boosted_score = score
        self.data = data
        self.time = datetime.datetime.now()
        self.active = True

    # get_id getter method
    def get_id(self):
        return self.id

    # get_time getter method
    def get_time(self):
        return self.time

    def get_score(self):
        return self.score

    def get_type(self):
        return self.type

    def get_data(self):
        return self.data

    def is_deleted(self):
        return not self.active

    def delete(self):
        self.active = False

    def boost_score(self, boost, start_over):
        self.boosted_score = (self.score if start_over
                                else self.boosted_score) * boost
