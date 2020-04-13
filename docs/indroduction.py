# division always returns float type(4/2) -> <class 'float'>
# floor division (get the integer) => 5 // 2 -> 2
# reminder       (of the division) => 5 %  2 -> 1
# power => 2 ** 3 -> 8; 5 ** 3 -> 125

# width = 20
# height = 5 * 9
# width * height
# prompt will show 900

# types -> int, float, Decimal, Fraction, complex
# https://docs.python.org/3/library/fractions.html#fractions.Fraction

# raw strings => r'C:\some\name' -> \n will not be scaped

# !!! -> All slice operations return a new list containing the requested
# elements. This means that the following slice returns a SHALLOW COPY of the
# list.

# https://docs.python.org/3/library/copy.html#shallow-vs-deep-copy

myList = [1, 2, 3, 4, 5]
print("myList memory address: {}".format(hex(id(myList))))
print("myList[0] memory address: {}".format(hex(id(myList[0]))))
print("myList[:] memory address: {}".format(hex(id(myList[:]))))
print("myList[:][0] memory address: {}".format(hex(id(myList[:][0]))))

# concat list
print([1, 2] + [3, 4])

### STRING METHODS
# str.capitalize()
# str.casefold()
# str.center(width[, fillchar])
# str.count(sub[, start[, end]])
# str.encode(enconding="utf-8", errors="strict")
# str.endswith(suffix[, start[, end]])
# str.expandtabs(tabsize=8)
# str.find(sub[, start[, end]])
# str.format(*args, **kwargs)
# str.format_map(mapping)
# str.index(sub[, start[, end]])
# str.isalnum()
# str.isalpha()
# str.isascii()
# str.isdecimal()
# str.isdigit()
# str.isidentifier()
# str.islower()
# str.isnumeric()
# str.isprintable()
# str.isspace()
# str.istitle()
# str.isupper()
# str.join(iterable)
# str.ljust()
# str.lower()
# str.lstrip([chars])
# str.partition(separator)
# str.replace(old, new[, count])
# str.rfind(sub[, start[, end]])
# str.rindex(sub[, start[, end]])
# str.rjust(width[, fillchar])
# str.rpartition(separator)
# str.rsplit(sep=None, maxplit=-1)
# str.rstrip([chars])
# str.split(sep=None, maxsplit=-1)
# str.splitlines([keepends])
#  *** https://docs.python.org/3/glossary.html#term-universal-newlines
# str.startswith(prefix[, start[, end]])
# str.strip([chars])
# str.swapcase()
# str.title()
# str.translate(table)
# str.upper()
# str.zfill(width)
