from functools import reduce

def suma(a,b):
    return a + b

rs = reduce(suma, [1, 2, 3, 4])
print(rs)