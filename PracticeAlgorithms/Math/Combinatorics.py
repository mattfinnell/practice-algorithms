from functools import reduce 

def factorial(n):
    if n == 0: 
        return 1

    return reduce(lambda acc, x: acc * x, range(1, n + 1))

def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def permutation(n, k):
    return factorial(n) / factorial(n - k)