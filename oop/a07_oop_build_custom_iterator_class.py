class Lineup:
  def __init__(self, players):
    self.players = players

  def __iter__(self):
    self.n = 0
    return self

  def __next__(self):
    if self.n < (len(self.players) - 1):
      player = self.players[self.n]
      self.n += 1
      return player
    elif self.n == (len(self.players) - 1):
      player = self.players[self.n]
      self.n = 0
      return player



astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))

