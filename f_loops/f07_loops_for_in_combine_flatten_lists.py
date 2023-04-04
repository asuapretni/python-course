legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]
print(raw_db)  # [['Alice', 'Bob'], ['Tiffany', 'Kristine']]



for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)

print(new_customers)  # ['Tiffany', 'Kristine', 'Alice', 'Bob']


# Exercise solved
def loop_over_list():
    numbers = [1, 2, 3, 4, 5, 6]
    result = []

    for number in numbers:
        result.append(number + 1)

    return result

print(loop_over_list())
