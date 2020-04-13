def to_base(x, b):
    return reversed(tuple(digits(x, b)))
    # tuple(digits(x, b))[::-1]

def digits(x, b):
    if x == 0: return
    yield x % b
    for d in to_base(x // b, b):
        yield d

print(list(digits(10, 2)))
