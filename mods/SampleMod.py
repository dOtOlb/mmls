import sys
import datetime
import operator
# this is to be updated further
sys.path.append("../lib/")
import Store

class SampleMod:
    """ a sample module implementation which presumes log-based pattern extraction """
    __init__(self):
        self.store = Store()

    # input_from_file method
    __input_from_file(fh):
        count_commands = 0
        for line in fh:
            count_commands = count_commands or (int(line) + 1)

            # extract into the internal store first
            self.store.add(line)

            count_commands -= 1
            if (count_commands == 0): break

    # run method
    __run():
        pass

    __input_from_file = input_from_file
    __run = run
