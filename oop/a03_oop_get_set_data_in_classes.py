class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    # example of java
    # def get_client():
    #     return self.client

    def formatter(self):
        return f'{self.client} owes: ${self.total}'


google = Invoice('Google', 100)

print(google.client)  # we can access the object elements without a getter function

# example of java
# print(google.get_client)

google.client = 'Yahoo'  # we can set values without a setter function

print(google.client)

# exercise solved
# Starter code
class Garage:
    def __init__(self, size):
        self.size = size
        self.cars = ["Ram", "Model 3"]

    def open_door(self):
        return "The door opens"


home = Garage(2)
# End of starter code
# print(home.cars)
home.cars = []

get_cars = home.cars
# print(get_cars)