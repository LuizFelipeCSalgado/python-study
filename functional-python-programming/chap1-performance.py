import timeit

print("((([] + [1]) + [2]) + [3]) + [4] took =\t",
      timeit.timeit("((([] + [1]) + [2]) + [3]) + [4]"))

print("[] + ([1] + ([2] + ([3] + [4]))) took =\t",
      timeit.timeit("[] + ([1] + ([2] + ([3] + [4])))"))
