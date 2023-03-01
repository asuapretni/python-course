teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

featured_team = teams.get('yankees', 'No featured team')
print(featured_team)

no_team = teams.get('mets', 'No featured team')  # prints the second argument cause there's no key named mets in the dictionary
print(no_team)
