import os.path
import sys


def exercise1(path):
    return sorted(list(set([os.path.splitext(i)[1] for i in os.listdir(path) if os.path.splitext(i)[1] != ''])))


def exercise2(directory, file):
    try:
        f = open(file, "wt")
        for path in os.listdir(directory):
            if path[0] == 'A':
                f.write(directory + '\\' + path + '\n')
        f.close()
        return "Written in file."
    except:
        raise Exception("Unable to open file.")


def exercise3(path):
    counter_dict = {}
    if os.path.isfile(path):
        try:
            f = open(path, "r")
            data = f.read()
            f.close()
            return data[-20:]
        except:
            raise Exception("Unable to open file.")
    else:
        for root, dirs, files in os.walk(path):
            for i in files:
                if os.path.splitext(i)[1] != '':
                    counter_dict[os.path.splitext(i)[1]] = counter_dict[os.path.splitext(i)[1]] + 1 if \
                        os.path.splitext(i)[
                            1] in counter_dict else 1
        return sorted([(key, value) for key, value in counter_dict.items()], key=lambda x: x[1], reverse=True)


def exercise4():
    return exercise1(sys.argv[1])


def exercise5(target, to_search):
    to_return = []
    if os.path.isfile(target):
        try:
            f = open(target, "r")
            data = f.read()
            f.close()
            if to_search in data:
                return [os.path.basename(target)]
        except:
            raise Exception("Unable to open file.")
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for i in files:
                path = os.path.join(root, i)
                try:
                    f = open(path, "r", encoding="cp437")
                    data = f.read()
                    f.close()
                    if to_search in data:
                        to_return.append(os.path.basename(path))
                except:
                    raise Exception("Unable to open file.")
    else:
        raise ValueError("Target is neither file nor directory.")
    return to_return


def callback(e):
    raise e


def exercise6(target, to_search, throw):
    to_return = []
    if os.path.isfile(target):
        try:
            f = open(target, "r")
            data = f.read()
            f.close()
            if to_search in data:
                return [os.path.basename(target)]
        except Exception("Unable to open file.") as e:
            throw(e)
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for i in files:
                path = os.path.join(root, i)
                try:
                    f = open(path, "r", encoding="cp437")
                    data = f.read()
                    f.close()
                    if to_search in data:
                        to_return.append(os.path.basename(path))
                except Exception("Unable to open file.") as e:
                    throw(e)
    else:
        e = ValueError("Target is neither file nor directory.")
        throw(e)
    return to_return


def exercise7(path):
    try:
        assert os.path.isfile(path), "Not a file"
        file_details = {"full_path": os.path.abspath(path), "file_size": os.stat(path).st_size,
                        "file_extension": os.path.splitext(path)[1], "can_read": os.access(path, os.R_OK),
                        "can_write": os.access(path, os.W_OK)}
        return file_details
    except Exception as e:
        raise e


def exercise8(path):
    abs_paths = []
    try:
        assert os.path.isdir(path), "Not a directory"
        for i in os.listdir(path):
            abs_paths.append(os.path.abspath(i))
        return abs_paths
    except Exception as e:
        raise e


if __name__ == '__main__':
    local_path = os.path.abspath(os.getcwd())
    print(f"exercise 1:\n{exercise1(local_path)}")
    file_path = local_path + "\\exercise2_output.txt"
    print(f"exercise 2:\n{exercise2(local_path, file_path)}")
    my_path = local_path + "\\Arandom.txt"
    print(f"exercise 3:\n{exercise3(local_path)}")
    print(f"exercise 4:\n{exercise4()}")
    target_dir = local_path + "\\mockFolder"
    target_file = target_dir + "\\someMoreRandom.txt"
    target_exception = target_dir + "\\gibberish"
    print(f"exercise 5:\n{exercise5(target_dir, 'laboris nisi')}")
    print(f"exercise 6:\n{exercise6(target_file, 'laboris nisi', callback)}")
    print(f"exercise 7:\n{exercise7(target_file)}")
    print(f"exercise 8:\n{exercise8(target_dir)}")