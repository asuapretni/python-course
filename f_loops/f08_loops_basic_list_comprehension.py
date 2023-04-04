num_list = range(1, 11)

cubed_nums = []
for num in num_list:
    cubed_nums.append(num ** 3)

# the same as 3 lines above in 1 line using list comprehension
cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)



# even numbers
num_list = range(1, 11)

even_numbers = []

for num in num_list:
    if num % 2 == 0:
        even_numbers.append(num)

# same using list comprehension
even_numbers = [num for num in num_list if num % 2 == 0]


print(list(num_list))
print(even_numbers)


# exercise solved
def list_comprehension():
    numbers = [1, 2, 3, 4, 5, 6]
    # Write your code here
    result = [num + 1 for num in numbers]

    return result
print(list_comprehension())