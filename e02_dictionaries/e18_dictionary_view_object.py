players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}
print(players.values())
print(list(players.values()))
print(list(players.values())[0])

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()
print(list(team_groupings))
print(list(team_groupings)[1][1][0])