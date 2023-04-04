post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from end
post = post[:-1]

# Removing elements from beggining
post = post[1:]

# Removing specific element (messy/not recommended)
post = list(post)  # change to list
post.remove('published')  # remove item/s
post = tuple(post)  # chage back to tuple

print(post)