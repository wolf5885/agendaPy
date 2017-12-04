#!/usr/bin/env python3

from menu import mainMenu
from  loadSave import save
from altaPersonas import hightPerson
from busqueda import search 
from eliminarPersona import remove

dairy = []


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
        remove(dairy)
        
                
save(dairy)
