def greeting(time_of_day, *args, **kwargs):
    print(f"Hi {' '.join(args)}, have a nice {time_of_day}!")
    if kwargs:
        print("This are your tasks:")
        for key, val in kwargs.items():
            print(f"{key} -> {val}")


greeting('Morning',  # Positinal argument
         'Kristine', 'M', 'Hudgens',  # items converted into a tuple
         First='Empty dishwasher',  # kwargs converted to a dictionery
         second='Take pupper outside',
         third='Math homework')