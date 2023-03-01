users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

users.remove('Jordan')

popped_user = users.pop()  # take the last element away from the list and return it so you can use it
print(popped_user)

del users[0]

print(users)