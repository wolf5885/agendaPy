from os import system
from menu import hightMenu

def hightPerson(dairy):
	while True:
		hightMenu()

		option = input("Seleccione una opción: ")

		if option in ["v", "V"]:
			break
		elif option in ["a", "A"]:
			dairy = hight(dairy)
	
	return dairy


def hight(dairy):
	person = {}

	person["lastName"] = input("Ingrese apellido: ")
	person["Name"] = input("Ingrese nombre: ")
	person["dni"] = int(input("Ingrese DNI: "))
	person["address"] = input("Ingrese dirección: ")
	person["phone"] = input("Ingrese teléfono: ")
	person["mail"] = input("Ingrese correo electrónico: ")

	dairy.append(person)

	return dairy
