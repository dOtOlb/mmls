import sys
import datetime
import operator

class InvertedIndex:
    """An implementation of the inverted index"""
    def __init__(self):
        self.index = {}

    # add method
    def add(self, lexicon_id, item_id):
        if lexicon_id not in self.index.keys():
            self.index[lexicon_id] = [item_id]
        elif item_id not in self.index[lexicon_id]:
            self.index[lexicon_id].append(item_id)

    # search method
    def search(self, lexicon_id):
        return [] if lexicon_id not in self.index.keys() else self.index[lexicon_id]

    # uniq method
    def uniq(self, seq):
        seen = set()
        seen_add = seen.add
        return [ x for x in seq if not (x in seen or seen_add(x)) ]

    def search_multi(self, lexicon_ids):
        result = []
        for lexicon_id in lexicon_ids:
            result += self.__search(lexicon_id)
        return self.__uniq(result)

    __add = add
    __search = search
    __uniq = uniq
    __search_multi = search_multi
