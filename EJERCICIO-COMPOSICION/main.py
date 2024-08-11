from gestorEdificios import gestorEdificios
ge = gestorEdificios()
def menu():
    print("------------------------")
    print("[1] Cargar Edificios y departamentos")
    print("[2] Mostrar nombres y apellidos")
    print("[3] Mostrar la Superficie Total de un edificio")
    print("[4] Mostrar el porcentaje de Superficie Total de un propietario")
    print("[5] Contar Departamentos con 3 dormitorios y mas de un baño")
    print("[6] Salir")

if __name__ == "__main__":
    menu()
    opcion = int(input("ingrese una opcion: "))
    while opcion != 6:
        if opcion == 1:
            ge.cargarEdificios()
        elif opcion == 2:
            nombre = input("Ingrese el nombre de un edificio: ")
            ge.mostrarDatosPropietarios(nombre)
        elif opcion == 3:
            print("Opcion 3")
            ge.mostrarSupTotalEdificio()
        elif opcion == 4:
            nombre = input("Ingrese el nombre de un propietario: ")
            ge.superficieDelProp(nombre)
            
        elif opcion == 5:
            print("Opcion 5")
        menu()
        opcion = int(input("ingrese una opcion: "))