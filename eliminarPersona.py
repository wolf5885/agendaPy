from menu import removeMenu

def remove(dairy):

    while True:

        check = 1
        dni = int(input("Escribir Dni: "))
    
        for busqueda in dairy:
            
            if dni == busqueda["dni"]:
                print(busqueda)
                dairy.remove(busqueda)
                print("Eliminado con exito")
                input("")
                check = 0
                return dairy
                

        if check == 1 :
            print("No se encontro el dni ingresado")
            input("")
