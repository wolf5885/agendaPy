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
    
    for busqueda in dairy:
        
        if dni == busqueda["dni"]:
            print(busqueda)
            check = 0
            if "si" == input("Usted esta seguro de eliminar al sujeto (si) o (no): "):
                dairy.remove(busqueda)
                print("Eliminado con exito")
                input("")
            return dairy
                

            if check == 1 :
                print("No se encontro el dni ingresado")
                input("")
       
