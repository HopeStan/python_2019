def neighbors(list_of_symbols):
    index = 0
    while index + 1 < len(list_of_symbols):
        yield (list_of_symbols[index], list_of_symbols[index + 1])
        index += 1


def get_pairs(list_of_symbols):
    list_of_symbols = [(x, y) for (x, y) in neighbors(list_of_symbols)]
    return list_of_symbols


def test(list_text):
    if get_pairs(list_text).__len__() == 0:
        print('None')
    else:
        print(get_pairs(list_text))


test(['cghn', 'fhdth', 'dyudytu', 1, 9, 12])
