def fact(number):
    if number == 0: return 1
    return number * fact(number - 1)


def facti(number):
    if number == 0: return 1
    f = 1
    for i in range(2, number + 1):
        f = f * i
    return f


def fastexp(a, n):
    if n == 0: return 1
    elif n % 2 == 1: return a * fastexp(a, n - 1)
    else:
        t = fastexp(a, n // 2)
        return t * t


if __name__ == '__main__':
    # for i in range(3, 10):
    #     print(i, fact(i))

    # for i in range(3, 10):
    #     print(i, facti(i))

    print(fastexp(3, 5))
    print(fastexp(3, 8))
    print(fastexp(4, 5))
    print(fastexp(4, 8))
