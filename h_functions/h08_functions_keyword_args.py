def greeting(**kwargs):
    # print(kwargs) -> {} are passed as a dictionary
    if kwargs:
        print(f"Hi {kwargs['first_name']} {kwargs['last_name']}, have a nice day!")
    else:
        print(f'Hi Guest, have a nice day!')

greeting()
greeting(first_name='CCC', last_name='LLL')


"""
def intro(**data):
    print("\nData type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))
        # print(f"{key} is {value}")


intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
"""