import sys
sys.path.insert(0, './libs')  # coloca el dir libs el primero de la lista donde buscar helper
import helper

# print(sys.path)  # muestra los dir donde esta buscando modulos


def render():
    print(helper.greeting('Tiffany', 'Hudgens'))


render()
