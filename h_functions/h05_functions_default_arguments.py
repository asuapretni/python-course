def greeting(name = 'Guest'):
    print(f'Hi, {name}')


greeting()  # no arg, use the default one
greeting('Karlos')


def some_function(collection = []):  # considered a bad practice to set a mutable argument (list)
    collection.append(1)
    print(id(collection))
    return collection

print(some_function())  # [1]

# Another part of the program
print(some_function())  # [1, 1] not same result as it is store in memory


# exercise solved
def counter(initial_count=0):
    return initial_count + 1


print(counter())
