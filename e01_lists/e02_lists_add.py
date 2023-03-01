"""
User Database Query
Kristine
Tiffany
Jordan
"""

users = ['Kristine', 'Tiffany', 'Jordan']

users.insert(1, 'Anthony')  # add item in a position
print(users)

users.append('Ian')  # add item
print(users)

print(users[2])
print([users[2]])  # still a list

users[4] = 'Brayden' # change item value
print(users)