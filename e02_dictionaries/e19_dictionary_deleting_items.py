teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

# del teams['astros']  # retuns keyerror if not exist

removed_team = teams.pop('yankees', 'No team found')  # returns values or 2nd argument if name not in dict.

print(teams)
print(removed_team)
