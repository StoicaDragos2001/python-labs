import re
from math import sqrt, ceil

import numpy as np


def exercise1(a, b):
    if b == 0:
        return a
    return exercise1(b, a % b)


def exercise2(ch_string):
    return len(([x for x in ch_string if x in "aeiouAEIOU"]))


def exercise3(first, second):
    return second.count(first)


def exercise4(text):
    return '_'.join([x.lower() for x in (re.findall('[A-Z][^A-Z]*', text))])


def exercise5(matrix):
    result = []
    bound = matrix.shape[0]
    for i in range(ceil(sqrt(matrix.shape[0]))):
        for char in matrix[i][i:bound - i]:
            result.append(char)
        for char in matrix[i + 1:-i - 1, -i - 1]:
            result.append(char)
        for char in matrix[-i - 1][i:bound - i][::-1]:
            result.append(char)
        for char in matrix[i + 1:-i - 1, i][::-1]:
            result.append(char)
    return ''.join(result)


def exercise6(number):
    return str(number) == str(number)[::-1]


def exercise7(text):
    return re.findall('[0-9]+', text)[0]


def exercise8(number):
    return exercise3('1', str(bin(number)))


def exercise9(text):
    letters_dict = {}
    for i in text.lower().replace(' ', ''):
        letters_dict[i] = letters_dict[i] + 1 if i in letters_dict else 1
    return max(letters_dict, key=letters_dict.get)


def exercise10(text):
    return exercise3(' ', ' '.join(text.split())) + 1


if __name__ == '__main__':
    print(f"Greatest common divisor between 20 and 5: {exercise1(20, 5)}")
    print(f"Number of vowels in 'This is some random text': {exercise2('This is some random text')}")
    print(f"Number of 'ab' in 'ababa': {exercise3('ab', 'ababa')}")
    print(f"Output of 'UpperCamelCase': {exercise4('UpperCamelCase')}")
    matrix_example = np.array([['f', 'i', 'r', 's'],
                               ['n', '_', 'l', 't'],
                               ['o', 'b', 'a', '_'],
                               ['h', 't', 'y', 'p']])
    print(matrix_example)
    print(f"Result: {exercise5(matrix_example)}")
    print(f"Is 1234321 a palindrome? {exercise6(1234321)}")
    print(f"First number found in 'extract 1234 or 5678' is {exercise7('extract 1234 or 5678')}")
    print(f"Number of bits with value 1 for number 24: {exercise8(24)}")
    print(f"Most common letter in 'an apple is not a tomato': {exercise9('an apple is not a tomato')}")
    print(f"The text 'I have  Python   exam' has {exercise10('I have  Python   exam')} words")
