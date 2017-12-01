#!/usr/bin/env python3

from menu import mainMenu
from  loadSave import save
from altaPersonas import hightPerson
	
dairy = []

while True:
	mainMenu()

	option = input("Elija una opción: ")

	if option in ["s", "S"]:
		break
	elif option in ["a", "A"]:
		dairy = hightPerson(dairy)

save(dairy)
