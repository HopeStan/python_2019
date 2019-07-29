def multiply(list):  # multiply elements in list of integer
    total, number_of_0 = 1, 0
    for i in list:
        if i != 0:
            total *= i
        else:
            number_of_0 += 1
            continue
    if number_of_0 > 1:
        total = 0
    return total


def foo_0(list_of_integers):  # return list of product//element
    try:
        list_of_integers = [multiply(list_of_integers) // i for i in list_of_integers]
    except ZeroDivisionError:
        list_of_integers = [multiply(list_of_integers) if i == 0 else 0 for i in list_of_integers]
    return list_of_integers


print(foo_0([1, 2, 3, 1, 3]))
print(foo_0([1, 2, 3, 0, 3]))
print(foo_0([1, 2, 0, 0, 3]))
