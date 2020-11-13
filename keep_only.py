import argparse
import os

from typing import Iterable, Dict
from collections import defaultdict

import utilities
import string


lst = string.ascii_uppercase


def generate_keep_dictionary(keepList):
    keepDict = {char: char for char in keepList}
    firstChar = 'א'
    lastChar = 'ת'
    for i in range(ord(firstChar), ord(lastChar) + 1):
        if chr(i) not in keepDict:
            keepDict[chr(i)] = lst[i % 22]
    return keepDict


def replace(content, dictionary):
    content = [char if char not in dictionary else dictionary[char]
               for char in content]
    utilities.protect_file_from_delete(args.output_file)
    with open(args.output_file, "w", encoding=utilities.ENCODING) as f:
        f.write(''.join(content))


def main():
    replace(utilities.read_utf8_encrypted_file(
        args.input_file), generate_keep_dictionary(args.keep))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("output_file", type=str)
    parser.add_argument("--keep", nargs="+")
    args = parser.parse_args()
    main()
