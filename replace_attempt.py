import argparse
import os

import db

import histogram
from typing import Iterable, Dict, List, Tuple
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


def sort_frequency_dictionary(dictionary: Dict[str, int]) -> List[Tuple[str, int]]:
    frequency = list(dictionary.items())
    frequency.sort(key=lambda item: item[1], reverse=True)
    return frequency


def make_most_prbable_dictionary() -> Dict[chr, chr]:
    frequency = sort_frequency_dictionary(db.FREQUENCY)
    text_histogram = histogram.find_histogram(
        utilities.read_utf8_encrypted_file(args.input_file))
    text_histogram = sort_frequency_dictionary(text_histogram)
    for i, (item, freq) in enumerate(frequency):
        frequency[i] = (chr(item), freq)

    characters = sum(map(lambda item: item[1], text_histogram))
    for i, (item, freq) in enumerate(text_histogram):
        text_histogram[i] = (item, freq / characters)

    return {char1: char2 for (char1, _), (char2, _) in zip(text_histogram, frequency)}


def main():
    if args.dict == "most-probable":
        dictionary = make_most_prbable_dictionary()
        for i, j in dictionary.items():
            print(f"x {i} x {j} x")
    else:
        dictionary = parse_dictionary()
    replace(utilities.read_utf8_encrypted_file(
        args.input_file), dictionary)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("output_file", type=str)
    parser.add_argument(
        "dict", help="Type most-probable to get most probable letters attachment")
    args = parser.parse_args()
    main()
