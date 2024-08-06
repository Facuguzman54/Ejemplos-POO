def menu():
    print("------------------------")
    print("[1] Cargar ")
    print("[2] ")
    print("[3] ")
    print("[4] ")
    print("[5] ")
    print("[6] Salir")

if __name__ == "__main__":
    menu()
    opcion = int(input("ingrese una opcion: "))
    while opcion != 6:
        if opcion == 1:
            print("Opcion 1")
           
        elif opcion == 2:
            print("Opcion 2")
        elif opcion == 3:
            print("Opcion 3")
           
        elif opcion == 4:
            print("Opcion 4")
            
        elif opcion == 5:
            print("Opcion 5")
        menu()
        opcion = int(input("ingrese una opcion: "))