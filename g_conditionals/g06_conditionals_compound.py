username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
    print('Access permitted')
else:
    print('you are not allowed')


# Same as above with nested conditionals
if (username == 'jonsnow' or email == 'jon@snow.com'):
    if password == 'thenorth':
        print('Access permitted')
    else:
        print('you are not allowed')


# Another example
logged_in = True
standard_user = True

if logged_in and not standard_user:
    print('Access the admin dashboard')
else:
    print('not acccess')


# exercise solved
def compound_conditional(number):
    if number > 0 and not number > 100:  # for number in range(1, 101):
        print("Success!")
    else:
        print("Failure...")

compound_conditional(100)