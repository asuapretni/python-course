import sys
sys.path.insert(0, './libs')  # coloca el dir libs el primero de la lista donde buscar helper
from helper import greeting

# print(sys.path)  # muestra los dir donde esta buscando modulos


def render():
    print(greeting('Tiffany', 'Hudgens'))


render()
