def auth(email, password):
    if email == 'Kristine@hudgens.com' and password == 'secret':
        print('Authorized')
    else:
        print('Not authorized')


auth('Kristine@hudgens.com', 'secret')


def counter(min, max):
    for num in range(min, max):
        print(num)


counter(6, 38)


# exercise solved
def greeting():
    print('hello')


greeting()
