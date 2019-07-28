def split_by_index(input_string: str, sep):
    List_of_words = []
    for index, symbol in enumerate(input_string):
        for i in sep:
            if index == i:
                List_of_words.append(input_string[:index])  # add words into list of words
                input_string = input_string[index:]  # del word from input string
    List_of_words.append(input_string[:])  # add last word into list os words
    return List_of_words


print(split_by_index('1234567891213', [2, 4, 5]))
print(split_by_index("no lusk", [20]))
