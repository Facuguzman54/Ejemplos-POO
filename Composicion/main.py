from GestorEdificios import GestorEdificios
ge = GestorEdificios()

def menu():
    print("=======================================")
    print("(1). Mostrar Edificio")
    print("(2). Mostrar la superficie total de un edificio")
    print("(3). Calcular el Porcentaje de un Inquilino")





if __name__ == "__main__":

    menu()
    opcion = int(input("Ingrese una Opcion: "))

    while opcion != 0:
        if opcion == 1:
            ge.mostrarEdificio(input("Ingresar nombre del edificio(Norte-Sur): "))
        elif opcion == 2:
            ge.calcularSuperficie(input("Ingresar nombre del edificio(Norte-Sur): "))
        elif opcion == 3:
            ge.porcentajeSuperficie(input("Ingresar Nombre y Apellido del Inquilino: "))
        
        

        
            





        menu()
        opcion = int(input("Ingrese una Opcion: "))