from menu import changeMenu
from menu import modificationMenu

def modification(dairy):
    
    while True:
        changeMenu()
        option = input("Ingrese opcion: ")
        if option in ["d", "D"]:
            dairy = searchModification(dairy)
        elif option in ["v", "V"]:
            break
  

def searchModification(dairy):
    check = 1
    dni = int(input("Escribir Dni: "))
    
    for busqueda in dairy:
        
        if dni == busqueda["dni"]:
            print(busqueda)
            check = 0
            if "si" == input("Usted quiere modificar a este sujeto (si) o (no): "):
                busqueda = optionModification(busqueda)
                dairy.append(busqueda)
                print("")
                return dairy
                

            if check == 1 :
                print("No se encontro el dni ingresado")
                input("")
                
def optionModification(busqueda):
    
    while True:
        modificationMenu()
        option = input(" Escribe la letra de la opcion: ")
        if option in ["e", "E"]:
            print(busqueda)
            busqueda["mail"] = input("Ingrese nuevo mail: ")
            print()
            print("Modificado con exito")
            print(busqueda)
            input("")
        elif option in ["d", "D"]:
            print(busqueda)
            busqueda["address"] = input("Ingrese nueva direccion: ")
            print()
            print("Modificado con exito")
            print(busqueda)
            input("")
        elif option in ["t", "T"]: 
            print(busqueda)
            busqueda["phone"] = input("Ingrese nuevo telefono: ")
            print()
            print("Modificado con exito")
            print(busqueda)
            input("")
        elif option in ["V", "v"]: 
            break

    return busqueda
        
        
        
