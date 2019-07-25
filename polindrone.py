def polindron(text):
    return text == text[::-1]

print(polindron('yey'))
print(polindron('hello'))
