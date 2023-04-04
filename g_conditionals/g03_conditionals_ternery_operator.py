role = 'admin'

auth = 'can access' if role == 'admin' else 'canot access'

if role == 'admin':
    print('can acess')
else:
    print('cannot access')


# exercise solved
language = "python"

language_check = True if language == 'python' else False
print(language_check)
