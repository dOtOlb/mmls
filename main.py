# Multi-modal load simulator
# Python version
import sys
import datetime
import operator

# import modules
import LogBasedMod

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-v', '--version', dest='ver', required=True, help="version 1 or 2")
    parser.add_argument('-m', '--module', dest='mod', required=True, help="module to use")
    return parser.parse_args()

def main():
    args = parse_args()

    if args.mod == 'log_based':
        m = LogBasedMod()

    m.run()
