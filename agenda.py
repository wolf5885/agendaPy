#!/usr/bin/env python3

from menu import menuPpal
from  loadSave import guardar
from altaPersonas import altaPersonas
	
agenda = []

while True:
	menuPpal()

	operation = input("Elija una opción: ")

	if operation in ["s", "S"]:
		break
	elif operation in ["a", "A"]:
		agenda = altaPersonas(agenda)

guardar(agenda)
