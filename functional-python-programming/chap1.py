# Imperative paradigms: procedural & object-oriented

# procedural computation
s = 0 # rely on assigment
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        s += n

print(s)

# state is defined by s and n

# ==============================

# object-oriented computation

m = list() # rely on assigment
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        m.append(n)

print(m)
print(sum(m))

class SummableList(list):
    def sum(self):
        s = 0
        for v in self.__iter__():
            s += v
        return s

o = SummableList() # rely on assigment
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        o.append(n)

print(o)
print(o.sum())


# accumulates a statefull collection object m

# ==============================

# functional approach

# the sum of the multiples of 3 and 5 can be defined in two parts:
# 1. The sum of a sequence of numbers
# 2. A sequence of values that pass a simple test condition, for example, being
# multiples of three and five

def sum_of_sequence(sequence):
    if len(sequence) == 0: return 0 # base case: states that a sum of a zero
                                    # length sequence is 0
    return sequence[0] + sum_of_sequence(sequence[1:]) # recursive case: states
                                           # that the sum of a sequence is the
                                           # first value plus the sum of the
                                           # rest of the sequence

def until(n, filter_func, value):
    if value == n: return [] # base case
    if filter_func(value): return [value] + until(n, filter_func, value + 1)
    else: return until(n, filter_func, value + 1)

mult_3_5 = lambda x: (x % 3 == 0) or (x % 5 == 0)

result = sum_of_sequence(until(10, mult_3_5, 0))
print('functional approach = ', result)

# hybrid functional approach

print('hybrid functional approach',
      sum(n for n in range(1, 10) if n % 3 == 0 or n % 5 == 0))
