# s = input()
# a = s.translate({39: '"', 34: "'"})
# print(a)
# 39--'
# 34--"


def re_symbol_1(text):
    text = text.translate({39: '"', 34: "'"})
    return text


print(re_symbol_1("""sdfg'dgf"fdgh'dfgh"Dgh'dfghdfg'd"""))


def symbol_split(text):
    spisok = text.split('"')
    for i in range(len(spisok)):
        spisok[i] = spisok[i].replace("'", '"')
    text = "'".join(spisok)
    return text


print(symbol_split("""srdg'dsfg"sdfgsfg'sdafg"sdfg:'"""))
