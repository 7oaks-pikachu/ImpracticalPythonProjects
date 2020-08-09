"""Loads a test file as a list

"""
import sys


def load(file):
    """Open a test file and return a list of lower case strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"{e}\n error opening {file}. Terminating program", file=sys.stderr)
        sys.exit(-1)
