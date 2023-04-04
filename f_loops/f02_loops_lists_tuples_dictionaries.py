# loop over list or tuple
# players = ('Altuve', 'Bregman', 'Correa', 'Gattis')
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
    print(player)

# loop over dictionary
players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player in players.items():
    print('Position', position)
    print('Player name', player)


# loop over a list of tuples
# converts dictionary into a list of tuples
# [('2b', 'Altuve'), ('3b', 'Bregman'), ('ss', 'Correa'), ('dh', 'Gattis')]
new_players = [(position, player) for position, player in players.items()]

for position, player in new_players:
    print('Position', position)
    print('Player name', player)
