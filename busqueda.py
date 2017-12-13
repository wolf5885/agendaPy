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

    for searcher in dairy:

        if lastName == searcher["lastName"]:

            print()
            print("Nombre: " + searcher["name"] )
            print("Apellido: " + searcher["lastName"])
            print("Dni: " + str(searcher["dni"]))
            print("Direccion: " + searcher["address"] )
            print("telefono: " + searcher["phone"] )
            print("Correo electronico: " + searcher["mail"])
            print()
            
            input("")
            check = 0
    if check == 1 :
        print("No se encontro apellido ingresado")
        input("")


def searchDni(dairy):
    
    check = 1
    dni = int(input("Escribir Dni: "))
    
    for searcher in dairy:
        
        if dni == searcher["dni"]:
            
            print()
            print("Nombre: " + searcher["name"] )
            print("Apellido: " + searcher["lastName"])
            print("Dni: " + str(searcher["dni"]))
            print("Direccion: " + searcher["address"] )
            print("telefono: " + searcher["phone"] )
            print("Correo electronico: " + searcher["mail"])
            print()
            
            input("")
            check = 0
                

    if check == 1 :
        print("No se encontro el dni ingresado")
        input("")


