from menu import removeMenu

def remove(dairy):

    while True:        
        removeMenu()
        option = input("Elija opcion: ")

        if option in ["d", "D"]:       
            dairy = removeOption(dairy)
        elif option in ["v", "V"]:
            break
        
    return dairy
        
        
        
        
def removeOption(dairy):
    
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
            
            check = 0
            if "si" == input("Usted esta seguro de eliminar al sujeto (si) o (no): "):
                dairy.remove(searcher)
                print("Eliminado con exito")
                input("")
            return dairy
                

            if check == 1 :
                print("No se encontro el dni ingresado")
                input("")
       
