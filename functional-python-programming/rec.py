def fact(number):
    if number == 0: return 1
    return number * fact(number - 1)


def facti(number):
    if number == 0: return 1
    f = 1
    for i in range(2, number + 1):
        f = f * i
    return f


if __name__ == '__main__':
    for i in range(3, 10):
        print(i, fact(i))

    for i in range(3, 10):
        print(i, facti(i))
