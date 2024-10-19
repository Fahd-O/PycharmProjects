import math


def comb(a, b):
    print(math.factorial(a) / (math.factorial(b) * math.factorial(a - b)))


comb(9, 2)
print(math.factorial(5))
