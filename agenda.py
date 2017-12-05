#!/usr/bin/env python3

from menu import mainMenu
from  loadSave import *
from altaPersonas import hightPerson
from busqueda import search 
from eliminarPersona import remove
from modificacion import modification

dairy = load()


while True:
    mainMenu()

    option = input("Elija una opción: ")

    if option in ["s", "S"]:
        break
    elif option in ["a", "A"]:
        dairy = hightPerson(dairy)
    elif option in ["b", "B"]:
        search(dairy)
    elif option in ["e", "E"]:
        dairy = remove(dairy)
    elif option in ["m", "M"]:
        dairy = modification(dairy)
        
                
save(dairy)
