import argparse
import os

from typing import Iterable, Dict
from collections import defaultdict

import utilities


def parse_dictionary():
    result = {}
    reverseDict = {}
    for elem in args.dict.split(":"):
        key, val = elem.split("=")
        assert len(key) == 1
        assert len(val) == 1
        result[key] = val
        reverseDict[val] = key

    for key, val in list(result.items()):
        if val not in result:
            while key in reverseDict:
                key = reverseDict[key]
            result[val] = key

    return result


def replace(content, dictionary):
    content = [char if char not in dictionary else dictionary[char]
               for char in content]
    utilities.protect_file_from_delete(args.output_file)
    with open(args.output_file, "w", encoding=utilities.ENCODING) as f:
        f.write(''.join(content))


def main():
    replace(utilities.read_utf8_encrypted_file(
        args.input_file), parse_dictionary())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("output_file", type=str)
    parser.add_argument("dict")
    args = parser.parse_args()
    main()
