usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
    if username == 'cersei':
        print(f'{username}, not allowed')
        continue
    else:
        print(f'{username}, allowed')


for username in usernames:
    if username == 'cersei':
        print(f'{username}, is at index {usernames.index(username)}')
        break
    print(username)