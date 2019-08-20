def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

# fib is NOT procedure cause returns None

what_type = fib(10) # will indeed print the values
print("\n")
print(what_type) # None
print(type(what_type)) # <class 'NoneType'>

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
# NO OVERLOAD
# def fib2(a, b):
#     print('overloaded!')

print(fib2(10))

def ask_ok(prompt: str, retries=4, reminder='Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ways to cal ask_ok
ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('Wanting to create new file?', 4, 'you can do it!')

ask_ok('first one = another question', retries=1)
ask_ok('second one = another question', retries=1, reminder="A REMIDER")
ask_ok('third one = another question', reminder="A REMIDER", retries=3)
