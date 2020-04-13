from decimal import *

def clean_decimal(text):
    if text is None: return text
    try:
        return Decimal(text.replace("$", "").replace(",", ""))
    except InvalidOperation:
        return text

def replace(data, first, second):
    return data.replace(first, second)

def remove(string: str, chars: str):
    if chars: return remove(replace(string, chars[0], ''), chars[1:])
    return string
