players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "DH": "Gattis",
  "OF": "Springer"
}

short_stop = players['ss']
second_base = players['2b']
designated_hitter = players['DH']  # BE CAREFUL is case sensitive
outfield = players['OF']
print(designated_hitter)

"""
# just an experiment but it works
def player_names(plays):
    list_of_players = []
    list_of_positions = []
    for (position, name) in plays.items():
        list_of_players.append(name)
        list_of_positions.append(position)
    return list_of_players, list_of_positions

print(player_names(players))
"""
