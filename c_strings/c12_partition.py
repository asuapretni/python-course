heading = "Python: An Introduction, and Python: Advanced"

header, _, subheader = heading.partition(': ')  # _ used to store data that is not useful

print(header)
print(subheader)

first, second, third = heading.partition(': ')  #partition returns a tuple

print(first)
print(second)
print(third)