from menu import searchMenu
	
def search(dairy):
    
    while True:
        searchMenu()
        
        option = input("Seleccione una opcion: ")

        if option in ["a", "A"]:
            searchLastname(dairy)
        elif option in ["d", "D"]:
            searchDni(dairy)
        elif option in ["v", "V"]:
            break

def searchLastname(dairy):
    
    lastName = input("Escribir apellido: ")
    check = 1

    for busqueda in dairy:

        if lastName == busqueda["lastName"]:
            print(busqueda)
            input("")
            check = 0
    if check == 1 :
        print("No se encontro apellido ingresado")
        input("")


def searchDni(dairy):
    
    check = 1
    dni = int(input("Escribir Dni: "))
    
    for busqueda in dairy:
        
        if dni == busqueda["dni"]:
            print(busqueda)
            input("")
            check = 0
                

    if check == 1 :
        print("No se encontro el dni ingresado")
        input("")


