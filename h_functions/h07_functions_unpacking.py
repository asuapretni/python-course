# *args take the rest of args that are passed and using .join(), joins them using a space or whatever you specify before join func
def greeting(time_of_day, *args):
    print(f"Hi {' '.join(args)}, I hope you a good {time_of_day}")
    # print(args) -> ('C.', 'M.', 'L.', 'ole') it is a tuple

greeting('evening', 'C.', 'M.', 'L.', 'ole')
