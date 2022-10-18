from math import sqrt
import numpy as np


def exercise1(n):
    fibo = [0, 1]
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    for i in range(n - 2):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo


def prime(x):
    if x > 1:
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
    else:
        return False
    return True


def exercise2(to_check):
    return [x for x in to_check if prime(x)]


def exercise3(a, b):
    intersection = [i for i in a if i in b]
    reunion = a.copy()
    reunion.extend(b)
    reunion = list(set(reunion))
    a_minus_b = [i for i in a if i not in b]
    b_minus_a = [i for i in b if i not in a]
    return (intersection, reunion, a_minus_b, b_minus_a)


def exercise4(notes, moves, start):
    order = [start]
    gama = len(notes)
    for i in moves:
        order.append((order[-1] + i) % gama)
    return [notes[i] for i in order]


def exercise5(matrix):
    new_matrix = matrix.copy()
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            if i > j:
                new_matrix[i][j] = 0
    return new_matrix


def exercise6(*argv, x):
    counter_dict = {}
    result = []
    for arg in argv:
        for i in arg:
            counter_dict[i] = counter_dict[i] + 1 if i in counter_dict else 1
    for value, counter in counter_dict.items():
        if counter == x:
            result.append(value)
    return result


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def exercise7(numbers):
    palindromes = []
    for i in numbers:
        if is_palindrome(i):
            palindromes.append(i)
    return (len(palindromes), max(palindromes))


def exercise8(data, x=1, flag=True):
    solution = []
    if flag:
        for word in data:
            selected = []
            for letter in word:
                if ord(letter) % x == 0:
                    selected.append(letter)
            solution.append(selected)
    else:
        for word in data:
            selected = []
            for letter in word:
                if ord(letter) % x != 0:
                    selected.append(letter)
            solution.append(selected)
    return solution


def exercise9(spectators):
    solution = []
    for i in range(spectators.shape[1]):
        col = spectators[::-1, i]
        for j in range(spectators.shape[0] - 1):
            if col[j] <= max(col[j + 1:]):
                solution.append((spectators.shape[0] - j - 1, i))
    return solution


def exercise10(*argv):
    solution = []
    matrix = []
    size = max([len(x) for x in argv])
    for arg in argv:
        arg.extend([None for _ in range(size - len(arg))])
        matrix.append(arg)
    matrix = np.array(matrix)
    for i in range(matrix.shape[1]):
        solution.append(tuple(matrix[:, i]))
    return solution


def sort_key(e):
    return e[:][1][2]


def exercise11(tuples):
    tuples.sort(key=sort_key)
    return tuples


def exercise12(words):
    rhymes = {}
    result = []
    for word in words:
        last2 = word[-2:]
        if last2 not in rhymes:
            rhymes[last2] = [word]
        else:
            rhymes[last2].append(word)
    for last2, words in rhymes.items():
        result.append(words)
    return result


if __name__ == '__main__':
    print(f"exercise 1:\n{exercise1(8)}")
    print(f"exercise 2:\n{exercise2([i for i in range(12)])}")
    print(f"exercise 3:\n{exercise3([i for i in range(12)], [i for i in range(7, 20)])}")
    print(f'exercise 4:\n{exercise4(["do", "re", "mi", "fa", "sol"], [2, 4, -6, 1], 2)}')
    ex5_result = exercise5([[x for x in range(1, 7)] for y in range(6)])
    print("exercise 5:")
    for i in ex5_result:
        print(i)
    print(f'exercise 6:\n{exercise6([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2)}')
    print(f"exercise 7:\n{exercise7([121, 123, 357753, 42, 11, 343, 59])}")
    print(f'exercise 8:\n{exercise8(["test", "hello", "lab002"], x=2, flag=False)}')
    exercise9_input = np.array([[1, 2, 3, 2, 1, 1],
                                [2, 4, 4, 3, 7, 2],
                                [5, 5, 2, 5, 6, 4],
                                [6, 6, 7, 6, 7, 5]])
    print(f'exercise 9:\n{exercise9(exercise9_input)}')
    print(f'exercise 10:\n{exercise10([1, 2, 3], [5, 6, 7], ["a", "b", "c"], [9])}')
    print(f"exercise 11:\n{exercise11([('abc', 'bcd'), ('abc', 'zza')])}")
    print(f"exercise 12:\n{exercise12(['ana', 'banana', 'carte', 'arme', 'parte'])}")
