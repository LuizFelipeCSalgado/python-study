def foo(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)

foo(1, 2, 3, 4, one='a', two='b', three='c')

def bar(a1, a2, a3, a4):
    print(a1, a2, a3, a4)

bar(1, 2, 3, 4)
bar(*[1, 2, 3, 4])

def sbar(one, two='with default'):
    print(one, two)

sbar(one=1, two='another one')
sbar(**{ 'one': 1, 'two': 'another one'})
sbar(**{ 'one': 1 })

add = lambda a, b: a + b
sub = lambda a, b: a - b

ten_plus_twelve = add(10, 20)
ten_minus_twelve = sub(10, 20)

print(ten_plus_twelve)
print(ten_minus_twelve)
