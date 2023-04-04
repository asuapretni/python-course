post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))  # return an in-memory identifier

post += ('published',)  # IMPORTANT the coma , to say that is a tuple not a mathematical parenthesis

print(id(post))  # return an in-memory identifier

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)
