from functools import reduce

# functional solution
def manual_exponent_f(num, exp):
    computed_list = [num] * exp  # we create a list needed to the reduce function as an argument
    return reduce((lambda total, element: total * element), computed_list)  # reduce iterates over the list (computed_list) till every list element is used in the function


# iterative approach
def manual_exponent_i(num, exp):
    counter = exp -1  # exp - 1 cause total = 1 otherwise we multiply it one more time
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

print(manual_exponent_f(5, 2))
print(manual_exponent_i(5, 2))