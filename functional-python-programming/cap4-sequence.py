from random import randint

flat = [randint(1, 100) for i in range(100)]
print(flat)
tuples = zip(flat[0::2], flat[1::2])
print("\n\n")
print(flat[0::2])
print(flat[1::2])
print("\n\n")
print(list(tuples))
print("\n\n")

make_sequences = lambda n: zip(*(flat[i::n] for i in range(n)))
print(list(make_sequences(1)))
print("\n\n")
print(list(make_sequences(2)))
print("\n\n")
print(list(make_sequences(3)))
