def next_(n, x):
    return ((x + n) / x) / 2

def repeat(f, a):
    yield a
    for v in repeat(f, f(a)):
        yield v

def within(epsilon, iterable):
    def head_tail(epsilon, current_item, iterable):
        next_item = next(iterable)
        if abs(current_item - next_item) < epsilon: return next_item
        return head_tail(epsilon, next_item, iterable)
    return head_tail(epsilon, next(iterable), iterable)

def sqrt(a0, epsilon, n):
    return within(epsilon, repeat(lambda x: next_(n, x), a0))

