class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)
snapchat = Invoice('Snapchat', 200)

print(google.formatter())
print(snapchat.formatter())




# exercise solved
class Garage:
    def __init__(self, size):
        self.size = size

    def open_door(self):
        return "The door opens"
        #  return f'Nº of cars: {self.size}'


home = Garage(2)  # instantiate with a garage size here
# print(home.open_door())