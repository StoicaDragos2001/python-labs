from typing import List
import re


def exercise2(*args, **kwargs: int) -> (int, str):
    try:
        return sum(kwargs.values())
    except TypeError:
        return "Can't make a sum."


def exercise3_method1(text: str) -> List:
    return [letter for letter in text if letter in "AEIOUaeiou"]


def exercise3_method2(text: str) -> List:
    return list(filter(lambda x: x in "AEIOUaeiou", text))


def exercise3_experiment(text: str) -> List:
    return re.findall(f'[{"AEIOUaeiou"}]', text)


def exercise4(*args, **kwargs) -> List:
    total = []
    total.extend([arg for arg in args])
    total.extend([val for (key, val) in kwargs.items()])
    return [i for i in total if
            type(i) == dict and len(i) >= 2 and (any([type(key) is str and len(key) >= 3 for key in i]))]


def exercise5(input_list: List) -> List:
    return [i for i in input_list if isinstance(i, (int, float))]


def exercise6(input_list: List) -> List:
    return list(
        map(lambda x, y: (x, y), filter(lambda a: a % 2 == 0, input_list), filter(lambda b: b % 2 == 1, input_list)))


def sum_digits(a):
    sum = 0
    while a:
        sum += a % 10
        a //= 10
    return sum


def exercise7(**kwargs) -> List:
    fibo = [int((((1 + 5 ** 0.5) / 2) ** i - ((1 - 5 ** 0.5) / 2) ** i) / 5 ** 0.5) for i in range(1000)]
    if "filters" in kwargs.keys():
        for condition in kwargs["filters"]:
            fibo = list(filter(condition, fibo))
    if "offset" in kwargs.keys():
        fibo = fibo[kwargs["offset"]:]
    if "limit" in kwargs.keys():
        fibo = fibo[:kwargs["limit"]]
    return fibo


def multiply_by_two(x):
    return x * 2


def multiply_by_three(x):
    return x * 3


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def inner_function(*args, **kwargs):
        print(f"Arguments are: {args},{kwargs}")
        return function(*args, **kwargs)

    return inner_function


def multiply_output(function):
    def inner_function(*args, **kwargs):
        return function(*args, **kwargs) * 2

    return inner_function


def augment_function(function, decorators):
    def inner_function(*args, **kwargs):
        a = function
        for decorator in decorators:
            a = decorator(a)
        return a(*args, **kwargs)

    return inner_function


def exercise9(pairs: List) -> List:
    return [{'sum': num1 + num2, 'prod': num1 * num2, 'pow': num1 ** num2} for (num1, num2) in pairs]


if __name__ == '__main__':
    print(f"exercise 2 - function:\n{exercise2(1, 2, c=3, d=4, e=2)}")
    lambda2 = lambda *args, **kwargs: sum(kwargs.values())
    print(f"exercise 2 - anonymous function:\n{lambda2(1, 2, c=3, d=4, e=2)}")

    print(f"exercise 3 - method 1:\n{exercise3_method1('Programming in Python is fun')}")
    print(f"exercise 3 - method 2:\n{exercise3_method2('Programming in Python is fun')}")
    lambda3 = lambda x: [i for i in x if i in "AEIOUaeiou"]
    print(f"exercise 3 - method 3:\n{lambda3('Programming in Python is fun')}")
    print(f"exercise 3 - method 4 (experiment):\n{exercise3_experiment('Programming in Python is fun')}")

    print(
        f"exercise 4:\n{exercise4({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True})}")

    print(f"exercise 5:\n{exercise5([1, '2', {'3': 'a'}, {4, 5}, 5, 6, 3.0])}")
    print(f"exercise 6:\n{exercise6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2])}")
    print(
        f"exercise 7:\n{exercise7(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2, offset=2)}")

    print("exercise 8.a:")
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)
    print(x)

    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)
    print(x)

    print("exercise 8.b:")
    augmented_multiply_by_three = multiply_output(multiply_by_three)
    x = augmented_multiply_by_three(10)
    print(x)

    print("exercise 8.c:")
    decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
    x = decorated_function(3, 4)
    print(x)

    print(f"exercise 9:\n{exercise9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)])}")
