from os import system
from menu import menuAlta

def altaPersonas(agenda):
	while True:
		menuAlta()

		operation = input("Seleccione una opción: ")

		if operation in ["v", "V"]:
			break
		elif operation in ["a", "A"]:
			agenda = alta(agenda)
	
	return agenda


def alta(agenda):
	persona = {}

	persona["apellido"] = input("Ingrese apellido: ")
	persona["nombre"] = input("Ingrese nombre: ")
	persona["dni"] = int(input("Ingrese DNI: "))
	persona["direccion"] = input("Ingrese dirección: ")
	persona["telefono"] = input("Ingrese teléfono: ")
	persona["correo"] = input("Ingrese correo electrónico: ")

	agenda.append(persona)

	return agenda
