import re
import os


def exercise1(text):
    return re.findall("\w+", text)


def exercise2(expr, source, size):
    return [word for word in source.split() if re.match(expr, word) and len(word) == size]
    # return [match for match in re.findall(expr, source) if len(match) == size]


def exercise3(text, list_of_regex):
    to_return = []
    for word in text.split():
        for regex in list_of_regex:
            if re.match(regex, word):
                to_return.append(word)
    return to_return


def exercise4(path, attrs):
    to_return = []
    with open(path, "r") as file:
        for line in file:
            if (all([re.search("\\w*" + item[0] + "=\"" + item[1] + "\"" + "\\w*", line.strip()) for item in
                     attrs.items()])):
                to_return.append(line.strip())
    return to_return


def exercise5(path, attrs):
    to_return = []
    with open(path, "r") as file:
        for line in file:
            if (any([re.search("\w*" + item[0] + "=\"" + item[1] + "\"" + "\w*", line.strip()) for item in
                     attrs.items()])):
                to_return.append(line.strip())
    return to_return


if __name__ == '__main__':
    print(f'exercise 1:\n{exercise1("Bla123 123 blabla bla1 bla 1")}')
    regex_string = "[\w\.-]+@[\w\.-]+"
    text = "random@gmail.com bla bla bla@gmail.com morebla blabla@gmail.com 123"
    print(f'exercise 2:\n{exercise2(regex_string, text, 16)}')
    regex_string2 = "[0-9]+"
    print(f'exercise 3:\n{exercise3(text, [regex_string, regex_string2])}')
    local_path = os.path.abspath(os.getcwd())
    print(
        f'exercise 4:\n{exercise4(local_path + "/random.xml", {"class": "url", "name": "url-form", "data-id": "item"})}')
    print(
        f'exercise 5:\n{exercise5(local_path + "/random.xml", {"class": "url", "name": "url-form", "data-id": "item"})}')
