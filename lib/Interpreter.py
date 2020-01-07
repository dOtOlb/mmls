import sys
import datetime
import operator

class Interpreter:
    """An implementation of the command interpreter"""
    def __init__(self, inverted_index, items, lexicon):
        self.inverted_index = inverted_index
        self.items = items
        self.lexicon = lexicon

    # interpret method
    def interpret(self, command):
        tokens = command.split()
        if tokens[0] == 'ADD':
            return self.__add(tokens[1], tokens[2], tokens[3],
                                command[len(tokens[1]) + len(tokens[2]) + len(tokens[3]) + 7:-1])
        elif tokens[0] == 'DEL':
            return self.__remove(tokens[1])
        elif tokens[0] == 'QUERY':
            return self.__query(tokens[1], command[len(tokens[1]) + 7:-1])
        elif tokens[0] == 'WQUERY':
            type_boost, id_boost = {}, {}
            boost_str_len = 0
            for i in range(int(tokens[2])):
                boost_str_len += len(tokens[i+3]) + 1
                boost_tokens = tokens[i+3].split(':')
                if is_type(boost_tokens[0]):
                    type_boost[boost_tokens[0]] = float(boost_tokens[1])
                else:
                    id_boost[boost_tokens[0]] = float(boost_tokens[1])
            return self.__wquery(tokens[1], type_boost, id_boost,
                                    command[len(tokens[1]) + len(tokens[2]) + boost_str_len + 9:-1])

    # add method
    def add(self, type, id, score, data):
        self.items[id] = ItemRecord(type, id, float(score), data)
        tokens = data.split()
        for token in tokens:
            lexicon_id = self.lexicon.add(token)
            self.inverted_index.add(lexicon_id, id)
        return ''

    # remove method
    def remove(self, id):
        self.items[id].delete()
        return ''

    # combine method
    def combine(self, lists):
        result = set(lists[0])
        for l in lists:
            result &= set(l)
        return [ item for item in result if not self.items[item].is_deleted() ]

    # query method
    def query(self, count, query_str):
        tokens = query_str.split()
        hit_lists = [ self.inverted_index.search_multi(self.lexicon.search(token))
                        for token in tokens ]
        final_hits = self.__combine(hit_lists)
        def key_func(*attrs):
            def f(item):
                return operator.attrgetter(*attrs)(self.items[item])
            return f

        final_hits.sort(key = key_func('score', 'time'), reverse = True)
        return (" ".join(final_hits[0:int(count)]) or " ")

    # wquery method
    def wquery(self, count, type_boost, id_boost, query_str):
        tokens = query_str.split()
        hit_lists = [ self.inverted_index.search_multi(self.lexicon.search(token))
                        for token in tokens ]
        final_hits = self.__combine(hit_lists)

        for hit in final_hits:
            self.items[hit].boost_score(1, True)
            if self.items[hit].get_type() in type_boost.keys():
                self.items[hit].boost_score(type_boost[self.items[hit].get_type()], False)
            if hit in id_boost.keys():
                self.items[hit].boost_score(id_boost[hit], False)

        def key_func(*attrs):
            def f(item):
                return operator.attrgetter(*attrs)(self.items[item])
            return f

        final_hits.sort(key = key_func('boosted_score', 'time'), reverse = True)
        return (" ".join(final_hits[0:int(count)]) or " ")

    __add = add
    __remove = remove
    __combine = combine
    __query = query
    __wquery = wquery
