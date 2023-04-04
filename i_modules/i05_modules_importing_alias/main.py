import sys
sys.path.insert(0, './libs')  # coloca el dir libs el primero de la lista donde buscar helper
import helper as h

# print(sys.path)  # muestra los dir donde esta buscando modulos


def render():
    print(h.greeting('Tiffany', 'Hudgens'))


render()

import math as m

m.sqrt(25)
