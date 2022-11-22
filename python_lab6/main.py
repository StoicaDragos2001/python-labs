import re
import os


def exercise1(input_text):
    return re.findall("\w+", input_text)


def exercise2(expr, source, size):
    return [word for word in source.split() if re.match(expr, word) and len(word) == size]
    # return [match for match in re.findall(expr, source) if len(match) == size]


def exercise3(input_text, list_of_regex):
    to_return = []
    for word in input_text.split():
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


def censor(s):
    if re.match("^[aeiou].*[aeiou]$", s.group(0)):
        return ''.join(["*" if i % 2 == 1 else s.group(0)[i] for i in range(len(s.group(0)))])
    return s.group(0)


def exercise6(input_text):
    return re.sub("\w+", censor, input_text)


def exercise7(cnp):
    # source: https://ro.wikipedia.org/wiki/Cod_numeric_personal_(Rom%C3%A2nia)
    return "Valid CNP" if re.match(
        "^[1-8]\d\d(0[1-9]|1[0-2])(0[1-9]|1\d|2\d|3\d)(0[1-9]|1\d|2\d|3\d|4[0-8]|5[1-2])\d\d\d\d",
        cnp) else "Not a valid CNP."


def exercise8(path):
    to_return = []
    for root, dirs, files in os.walk(path):
        for file in files:
            condition1, condition2 = 0, 0
            if re.match("^[aeiou].*[aeiou]$", os.path.splitext(file)[0]):
                condition1 = 1
            with open(os.path.join(root, file), encoding="utf-8") as f:
                for line in f:
                    for word in line.split():
                        if re.match("^[aeiou].*[aeiou]$", word):
                            condition2 = 1
                            break
            if condition1 and condition2:
                to_return.append(">>" + file)
            elif condition1 or condition2:
                to_return.append(file)
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
    print(f'exercise 6:\n{exercise6("This is some random example for the exercise")}')
    print(f'exercise 7:\n{exercise7("1460913400088")}')
    print(f'exercise 8:\n{exercise8(local_path + "/random_folder")}')
