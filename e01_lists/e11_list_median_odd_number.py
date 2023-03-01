import math
"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sale_prices)

first_sale_items = sorted_list[:math.floor(num_of_sales/2)]
last_sale_items = sorted_list[-(math.floor(num_of_sales/2)):]

half_slice = math.floor(num_of_sales/2)
median = sorted_list[half_slice:half_slice+1]

print(sorted_list)
print(first_sale_items)
print(last_sale_items)
print(median)


# Solution using statistics lybrary
# from statistics import median
# sorted_list = sorted(sale_prices)
# middle_el_list = median(sorted_list)
# print(middle_el_list)

# My solution
# import math
# sorted_list = sorted(sale_prices)
# lenght = len(sorted_list)
# middle = math.floor(lenght / 2)
# medium_el = sorted_list[middle:(middle+1)]  -> returns list
# medium_el = sorted_list[middle]  -> returns integer

# print(middle)
# print(sorted_list)
# print(medium_el)

# media aritmetica
# from functools import reduce
# sum = reduce((lambda total, element : total + element), sale_prices)
# media = sum / len(sale_prices)

# print(media)