class Invoice:

    def greeting(self):  #self needed as argument into classes
        return 'Hi there!'


inv_one = Invoice()  # one instance, needed to use the class
print(inv_one)
print(inv_one.greeting())

inv_two = Invoice()  # another instance of the class
print(inv_two)
print(inv_two.greeting())



# exercise solved
class Garage:

    def open_door(self):
        return 'The door opens'


home = Garage()

print(home.open_door())
