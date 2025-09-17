def word_count(text):
    words = text.split()
    return len(words)


def char_count(text):
    char = {}
    lower = text.lower()
    for i in lower:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
    return char

def sort_on(items):
    li = []
    for k, v in items.items():
        li.append({"char": k, "num": v})
    li.sort(key=lambda x: x["num"], reverse=True)
    # del li[0]  # remove space character entry
    li = [x for x in li if x["char"].isalpha()]  # remove non-alphabetic characters
    # a = []
    # for i in li:
        # a.append(f"'{i["char"]}': {i["num"]}")
    return li