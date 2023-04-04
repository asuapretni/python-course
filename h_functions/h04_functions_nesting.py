def greeting(first, last):
    def full_name():
        return f'{first} {last}'
    return f'Hi, {full_name()}!'

print(greeting('Kristine', 'Hudgens'))


# same as above but nested
"""
def full_name(first, last):
    return f'{first} {last}'


kristine = full_name('Kristine', 'Hudgends')


def greeting(name):
    print(f'Hi {name}!')


greeting(kristine)
"""


# exercise solved
def greeting(name):
    return f'Hello, {name}'

print(greeting('Carlos'))
