from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
initial_value = 10
result = reduce(add, numbers, initial_value)
print(result)  # 25 (10 + 1 + 2 + 3 + 4 + 5)

