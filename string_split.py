def string_split(input_string, sep):
    List_of_words = []
    for symbol in input_string:
        if symbol == sep:
            index = input_string.index(sep)
            List_of_words.append(input_string[:index])
            input_string = input_string[index+1:]
    return List_of_words


print(string_split('0 12 231654 354 546545 54 2221 ', ' '))