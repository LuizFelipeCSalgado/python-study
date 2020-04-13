import math

def pfactors(number):
    if number % 2 == 0:
        yield 2
        if number // 2 > 1:
            yield from pfactors(number // 2)
        return
    for i in range(3, int(math.sqrt(number) + .5) + 1, 2):
        if number % i == 0:
            yield i
            if number // i > 1:
                yield from pfactors(number // i)
            return 
    yield number

def pfactorsr(number):
    def factor_n(number, n):
        if n * n > number:
            yield number
            return
        if number % n == 0:
            yield n
            if number // n > 1:
                yield from factor_n(number // n, n)
        else:
            yield from factor_n(number, number + 2)
    if number % 2 == 0:
        yield 2
        if number // 2 > 1:
            yield from pfactorsr(number // 2)
        return
    yield from factor_n(number, 3)

f = lambda x: x ** 3
g = lambda x: (x ** 2) + 2

