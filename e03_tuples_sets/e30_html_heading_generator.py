# My solution using a dictionary as source
def heading_generator(headings):
    for title, val in headings.items():
        print(f'<h{val}>{title}</h{val}>')

my_headings = {
    'First': '1',
    'second': '2'
}

heading_generator(my_headings)



# Solution oficial
def heading_generator(title, heading_type):
    return f'<h{heading_type}>{title}</h{heading_type}>'

print(heading_generator('Hi there', 3))


# Another solution converting the dictionary into a list of tuples
# and use it to generate the html
new_list = [(title, val) for title, val in my_headings.items()]

def heading_generator_2(list_items):
  for title, val in list_items:
        print(f'<h{val}>{title}</h{val}>')

heading_generator_2(new_list)
