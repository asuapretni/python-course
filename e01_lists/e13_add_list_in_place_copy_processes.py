tags = ['python', 'development', 'tutorials', 'code']

# Nope
# tags[-1] = 'Programming'
# tags.extend('Programming')
# tags.extend(['Programming'])  # Add item to tags

mew_tags = tags + ['Programming']  # right way to create a new list with the item added

print(mew_tags)
print(tags)