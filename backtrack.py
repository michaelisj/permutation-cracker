import utilities

import db
import histogram


def get_permutation_score(content):
    return sum(content.count(word) for word in db.WORDS_DB)


def get_probability_of_permutation(frequency_table, permutation):
    p = 1.0
    for char in db.CHARACTERS:
        prob = frequency_table[permutation[char]] / db.FREQUENCY[char]
        p *= min(prob, 1/prob)

    return p


def find_histogram(content):
    dictionary = histogram.find_histogram(content, 1)
    result = {}
    for char in db.CHARACTERS:
        result[char] = dictionary[chr(char)] / len(content)
    return result


def read_file(path):
    return utilities.read_utf8_encrypted_file(path).replace(" ", "")


def generate_permutations(*lists):
    for lst in lists:
        for index, char in lst:
            lst[index] = ord(char)
    return lists