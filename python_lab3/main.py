import numpy as np


def exercise1(list1, list2):
    sets = []
    set1, set2 = set(list1), set(list2)
    sets.append(set1.intersection(set2))
    sets.append(set1.union(set2))
    sets.append(set1.difference(set2))
    sets.append(set2.difference(set1))
    return sets


def exercise2(text):
    counter_dict = {}
    for _ in text.replace(" ", ""):
        counter_dict[_] = counter_dict[_] + 1 if _ in counter_dict else 1
    return counter_dict


def exercise3(dict1, dict2):
    result = True
    for k1, k2 in zip(dict1.keys(), dict2.keys()):
        if k1 != k2:
            result = False
        if type(dict1[k1]) == dict and type(dict2[k2]) == dict:
            exercise3(dict1[k1], dict2[k2])
        else:
            if dict1[k1] != dict2[k1]:
                result = False
    return result


def build_xml_element(tag, content, href, _class, id):
    return '<' + tag + ' href=\\' + '"' + href + ' \\ ' + '"' + '_class = \\' + '" ' + _class + ' \\ "id = \\" ' + id + ' \\ "> ' + content + ' </' + tag + '>'


def exercise5(rules, dict):
    for j in dict.keys():
        if j not in np.array(list(r))[:, 0]:
            return False
    rules = list(rules)
    for key in dict.keys():
        for rule in rules:
            if key in rule:
                if dict[key].startswith(rule[1]) and dict[key].endswith(rule[3]) and (
                        rule[2] in dict[key] and dict[key].startswith(rule[2]) == False and dict[key].endswith(
                    rule[2]) == False):
                    pass
                else:
                    return False
    return True


def exercise6(data):
    data_set = set(data)
    for i in range(len(data_set)):
        data.pop(i)
    return len(data_set) - len(set(data)), len(set(data))


def exercise7(*args):
    dictionary = {}
    for i in range(0, len(args)):
        for j in range(i + 1, len(args)):
            arg1 = str(args[i])
            arg2 = str(args[j])
            operations = exercise1(args[i], args[j])
            dictionary[arg1 + " | " + arg2] = operations[0]
            dictionary[arg1 + " & " + arg2] = operations[1]
            dictionary[arg1 + " - " + arg2] = operations[2]
            dictionary[arg2 + " - " + arg1] = operations[3]
    return dictionary


def exercise8(mapping):
    visited = []
    val = mapping['start']
    visited.append(val)
    while mapping[val] not in visited:
        val = mapping[val]
        visited.append(val)
    return visited


def exercise9(*args, **kwargs):
    counter = 0
    for arg in args:
        if arg in kwargs.values():
            counter += 1
    return counter


if __name__ == '__main__':
    print(f"exercise 1: {exercise1([_ for _ in range(3, 14)], [_ for _ in range(7, 20)])}")
    print(f"exercise 2: {exercise2('Ana are mere')}")
    dictionary1 = {'programare': {'Python': 'laborator', 'sala': {'nume': 'C403', 'etaj': 2}}, 'random': [1, 2, 3]}
    dictionary2 = {'programare': {'Python': 'laborator', 'sala': {'nume': 'C403', 'etaj': 2}}, 'random': [1, 2, 3]}
    print(f"exercise 3: {exercise3(dictionary1, dictionary2)}")
    print(
        f'exercise 4: {build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")}')
    r = {("key1", "come", "inside", "out"), ("key2", "this", "middle", "valid")}
    d = {"key1": "come inside, it's too cold out", "key2": "this middle is valid"}
    print(f"exercise 5: {exercise5(r, d)}")
    print(f"exercise 6: {exercise6([1, 2, 3, 4, 5, 2, 2, 3, 4])}")
    print(f"exercise 7: {exercise7({1, 2, 3}, {2, 3, 4}, {1, 3, 4, 5})}")
    print(
        f"exercise 8: {exercise8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})}")
    print(f"exercise 9: {exercise9(1, 2, 3, 4, x=1, y=2, z=3, w=5)}")
