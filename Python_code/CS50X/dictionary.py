words = set()


def check(word):
    if word.lower() in words:
        return True
    else:
        return False


def load(dictionary):
    try:
        with open(dictionary, "r") as file:
            for line in file:
                word = line.rstrip()
                words.add(word)
                return True
    except FileNotFoundError:
        print(f" The file {dictionary} was not found.")
        return False

def size():
    return len(words)


def unload():
    return True
