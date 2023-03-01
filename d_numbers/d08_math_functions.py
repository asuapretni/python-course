import math

loss = -20.25
product_cost = 89.99

print(abs(loss))
print(math.floor(product_cost))  # round down
print(math.ceil(product_cost))  # round up
print(abs(math.floor(loss)))  # first math.floor -21 -> then abs 21
print(round(product_cost))  # rounds depending on decimals
print(math.sqrt(product_cost))
print(math.pow(5, 2))  # returns float
print(5 ** 2)  # returns integer