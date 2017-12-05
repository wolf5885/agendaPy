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
  
    return dairy

def searchModification(dairy):
    check = 1
    dni = int(input("Escribir Dni: "))
    
    for searcher in dairy:
        
        if dni == searcher["dni"]:
            print(searcher)
            check = 0
            if "si" == input("Usted quiere modificar a este sujeto (si) o (no): "):
                searcher = optionModification(searcher)
                dairy.append(searcher)
                print("")
                return dairy
                

            if check == 1 :
                print("No se encontro el dni ingresado")
                input("")
                
def optionModification(searcher):
    
    while True:
        modificationMenu()
        option = input(" Escribe la letra de la opcion: ")
        if option in ["e", "E"]:
            print(searcher)
            searcher["mail"] = input("Ingrese nuevo mail: ")
            print()
            print("Modificado con exito")
            print(searcher)
            input("")
        elif option in ["d", "D"]:
            print(searcher)
            searcher["address"] = input("Ingrese nueva direccion: ")
            print()
            print("Modificado con exito")
            print(searcher)
            input("")
        elif option in ["t", "T"]: 
            print(searcher)
            searcher["phone"] = input("Ingrese nuevo telefono: ")
            print()
            print("Modificado con exito")
            print(searcher)
            input("")
        elif option in ["V", "v"]: 
            break

    return searcher
        
        
        
