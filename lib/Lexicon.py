import sys
import datetime
import operator

class Lexicon:
    """
    An implementation of the corpus
    To Do: add another getter call for the corpus
    """
    def __init__(self):
        self.corpus = {}
        self.sorted_terms = []

    # add method
    def add(self, lexicon):
        lexicon_lower = lexicon.lower()
        if lexicon_lower not in self.corpus.keys():
            self.sorted_terms.append(lexicon_lower)
            self.sorted_terms.sort()
            self.corpus[lexicon_lower] = len(self.corpus.keys())

        return self.corpus[lexicon_lower]

    # get_id method
    def get_id(self, lexicon):
        lexicon_lower = lexicon.lower()
        return (None if lexicon_lower not in self.sorted_terms
                        else self.corpus[lexicon_lower])

    # search method
    def search(self, lexicon):
        lexicon_lower = lexicon.lower()
        if not self.sorted_terms:
            return []

        # initialize the variables used
        matches = []
        max_index = len(self.sorted_terms) - 1
        min_index = 0
        index = -1

        if lexicon_lower > self.sorted_terms[max_index]:
            return []
        if lexicon_lower == self.sorted_terms[max_index]:
            matches.append(self.__get_id(lexicon))
            index = max_index
        elif lexicon_lower == self.sorted_terms[min_index]:
            matches.append(self.__get_id(lexicon))
            index = min_index
        elif lexicon_lower > self.sorted_terms[min_index]:
            index = (max_index + min_index) // 2
            while index != min_index:
                if self.sorted_terms[index] == lexicon_lower:
                    matches.append(self.__get_id(lexicon_lower))
                    break
                elif self.sorted_terms[index] < lexicon_lower:
                    min_index = index
                else:
                    max_index = index
                index = (max_index + min_index) // 2

        index = index + 1
        while index < len(self.sorted_terms):
            if self.sorted_terms[index].startswith(lexicon_lower):
                matches.append(self.__get_id(self.sorted_terms[index]))
                index = index + 1
            else:
                break

        return matches

    __add = add
    __get_id = get_id
    __search = search
