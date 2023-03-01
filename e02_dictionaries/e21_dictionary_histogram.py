"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

# My solution
def histogram(dict):

    for (coorp, val) in dict.items():
            print(coorp[0][0] + ' ' + (val * '$') + ' ' + str(val))


sales = {
    'google': 10,
    'facebook': 6,
    'twitter': 4,
    'offline': 12,
}

histogram(sales)  # call it that way to avoid None as function has no return

# oficial solution
print('g ' + sales['google'] * '$')
print('f ' + sales['facebook'] * '$')
print('t ' + sales['twitter'] * '$')
print('o ' + sales['offline'] * '$')

# print(histogram(sales))  # cause double print statement it adds a None

# print(sales.items())
# print(list(sales.keys())[0][0])