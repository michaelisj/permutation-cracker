import argparse
import csv

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


def main():
    content = utilities.read_utf8_encrypted_file(args.input_file)
    histogram = find_histogram(content, args.longest_sequence)
    if args.all and args.longest_sequence > 1:
        for i in range(1, args.longest_sequence):
            histogram.update(find_histogram(content, i))
    # NOTE: This is inexact, as there are less triplets than characters,
    #   but good enough for small numbers
    format_histogram_to_file(histogram, args.output_file,
                             len(content), args.min_occurrences)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("output_file", type=str)
    parser.add_argument("--longest-sequence", "-n", type=int, default=1)
    parser.add_argument("--min-occurrences", "-m", type=int, default=2)
    parser.add_argument("--all", "-a", action="store_true")
    args = parser.parse_args()
    main()
