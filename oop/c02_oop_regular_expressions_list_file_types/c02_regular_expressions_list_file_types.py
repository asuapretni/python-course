import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):  # looks in actual dir
        if fnmatch.fnmatch(file, "*.txt"):
            print('Text files:', file)

        if fnmatch.fnmatch(file, "*.py"):
            print('Python files:', file)

        if fnmatch.fnmatch(file, "*.rb"):
            print('Ruby files:', file)

        if fnmatch.fnmatch(file, "*.yml"):
            print('Yaml files:', file)

list_files()


# same as above using filter, and better cause it returns a file list
def other_file_list():
    files = os.listdir('.')
    txt_files = fnmatch.filter(files, '*.txt')
    py_files = fnmatch.filter(files, '*.py')
    rb_files = fnmatch.filter(files, '*.rb')
    yml_files = fnmatch.filter(files, '*.yml')

    print('\n')
    print('My Txts:', txt_files)
    print('My Py:', py_files)
    print('My Ruby:', rb_files)
    print('My Yaml:', yml_files)
    print('\n')

other_file_list()


players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]
print("2nd base players:", second_base_players)


# same as above using filter instead of for loop and fnmatchcase
second_base_players = fnmatch.filter(players, "* 2B")
print("2nd base players:", second_base_players)

