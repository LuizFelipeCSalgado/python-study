#!/usr/bin/python3

def dispatch_dict(operator, x, y):
    operations = {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }
    operation = operations.get(operator, lambda: None)
    return operation()
