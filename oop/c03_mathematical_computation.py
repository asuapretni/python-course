def pretty_price(gross_price, extension):
    if isinstance(extension, int):  # check if extension is an int
        extension = extension * 0.01
    return int(gross_price) + extension


print(pretty_price(4.50, 0.95))
print(pretty_price(94.9, 27))



