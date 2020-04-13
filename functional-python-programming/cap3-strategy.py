import collections

# OO approach
class CalculateStrategy:
    def __init__(self, first, second):
        self.first = first
        self. second = second

    def execute(self): pass

class SumStrategy(CalculateStrategy):
    def execute(self):
        return self.first + self.second

class MultiplyStrategy(CalculateStrategy):
    def execute(self):
        return self.first * self.second

# callable approach
class Mersenne(collections.Callable):
    def __init__(self, algorithm):
        self.pow2 = algorithm

    def __call__(self, arg):
        return self.pow2(arg) - 1

def shifty(number):
    return 1 << number

def multy(number):
    if number == 0: return 1
    return 2 * multy(number - 1)

def faster(number):
    if number == 0: return 1
    if number % 2 == 1: return 2 * faster(number - 1)
    quotient_by_two = faster(number // 2)
    return quotient_by_two ** 2

if __name__ == '__main__':
    sumStrategy = SumStrategy(5, 5) # child of CalculateStrategy
    multiplyStrategy = MultiplyStrategy(5, 5) # child of CalculateStrategy
    print(f'sumStrategy.execute() = {sumStrategy.execute()}')
    print(f'multiplyStrategy.execute() = {multiplyStrategy.execute()}')

    mersenne_shifty = Mersenne(shifty)
    mersenne_multy = Mersenne(multy)
    mersenne_faster = Mersenne(faster)

    print(mersenne_shifty(4))
    print(mersenne_multy(5))
    print(mersenne_faster(6))

