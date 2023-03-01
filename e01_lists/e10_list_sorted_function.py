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

# sorted_list = sale_prices.sort()
# print(sorted_list) -> None

sorted_list = sorted(sale_prices, reverse=True)
print(sorted_list)
print(sale_prices)