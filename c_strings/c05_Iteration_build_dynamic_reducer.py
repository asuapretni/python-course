import operator
from functools import reduce
"""
dynamic_reducer([1, 2, 3], '+') # 6
dynamic_reducer([1, 2, 3], '-') # -
dynamic_reducer([1, 2, 3], '*') # 6
dynamic_reducer([1, 2, 3], '/') # -
"""

def dynamic_reducer(collection, op):
    # dictionary
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    return reduce((lambda total, element : operators[op](total, element)), collection)
    # reduce(function, parameter) -> repeteadly executes func till every param in collection is used -> [1, 2, 3]
    # function -> lambda total, element : operators[op](total, element)
    # depending on the op passed operators[op] could be ex: operator.add(total, element)

# variable = reduce(lambda total, element: operator.add(total, element), [1, 2, 3])
# print(variable)

print(dynamic_reducer([1, 2, 3], '+'))

print(dynamic_reducer([1, 2, 3], '-'))

print(dynamic_reducer([1, 2, 3], '*'))

print(dynamic_reducer([1, 2, 3], '/'))