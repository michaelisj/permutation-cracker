import argparse
import csv
import re

from typing import Iterable, Dict
from collections import defaultdict

import utilities


def find_histogram(string: str, n=1) -> Dict[str, int]:
    """Finds histogram of elements inside a string,
    possible of sequences as well

    Args:
        string (str): String to search for histograms inside
        n (int, optional): Size of sequence. Defaults to 1.
    """
    string = string.replace(" ", "")
    if n < 1:
        raise ValueError("n must be at least 1, got {}".format(n))

    result = defaultdict(lambda: 0)
    for i in range(len(string) - n + 1):
        result[string[i:i+n]] += 1

    return result


def format_histogram_to_file(histogram: Dict[str, int], outFilePath: str,
                             numberOfElements: int, minOccurrences: int = 1):
    UTF8_MAGIC = b"\xef\xbb\xbf"

    histogram = list(histogram.items())
    histogram.sort(key=lambda var: var[1], reverse=True)

    utilities.protect_file_from_delete(outFilePath)
    with open(outFilePath, "wb") as f:
        f.write(UTF8_MAGIC)

    with open(outFilePath, "a", newline='', encoding=utilities.ENCODING) as f:
        writer = csv.writer(f)
        writer.writerow("Element,Frequency,Occurrences".split(","))
        for element, occurrences in histogram:
            if occurrences < minOccurrences:
                continue
            frequency = "{:.4f}".format(occurrences / numberOfElements)
            writer.writerow([element, frequency, occurrences])


def print_histogram(histogram, contentLen):
    histogram = list(histogram.items())
    histogram.sort(key=lambda var: var[1], reverse=True)
    for element, occurrences in histogram:
        if occurrences >= args.min_occurrences:# and element.count(args.initial):
            frequency = "{:.4f}".format(occurrences / contentLen)
            print([f"x {element} x", frequency, occurrences])


def main():
    content = utilities.read_utf8_encrypted_file(args.input_file)
    if args.regex is not None:
        content = content.replace(" ", "")
        lst = re.findall(args.regex, content)
        d = defaultdict(lambda: 0)
        for x in lst:
            d[x] += 1
        print_histogram(d, len(content))
        raise SystemExit()
    histogram = find_histogram(content, args.longest_sequence)
    if args.all and args.longest_sequence > 1:
        for i in range(1, args.longest_sequence):
            histogram.update(find_histogram(content, i))
    # NOTE: This is inexact, as there are less triplets than characters,
    #   but good enough for small numbers
    if not args.stdout:
        format_histogram_to_file(histogram, args.output_file,
                                 len(content), args.min_occurrences)
    else:
        histogram = list(histogram.items())
        histogram.sort(key=lambda var: var[1], reverse=True)
        for element, occurrences in histogram:
            if occurrences >= args.min_occurrences and element.count(args.initial):
                frequency = "{:.4f}".format(occurrences / len(content))
                print([f"x {element} x", frequency, occurrences])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("output_file", type=str, default=None)
    parser.add_argument("--longest-sequence", "-n", type=int, default=1)
    parser.add_argument("--min-occurrences", "-m", type=int, default=2)
    parser.add_argument("--min-rate", "-r", type=float, default=None)
    parser.add_argument("--all", "-a", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    parser.add_argument("--initial", default="")
    parser.add_argument("--regex", default=None)
    args = parser.parse_args()
    if args.output_file == 'stdout':
        args.stdout = True
        args.output_file = None
    main()
