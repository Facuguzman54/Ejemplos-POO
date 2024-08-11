from Lista import Lista
from Locales import Locales
from Nacionales import Nacionales
lista = Lista()
def menu():
    print("-------------------")
    print("[1] Insertar objetos al final de la colección")
    print("[2] Listar clientes Nacionales")
    print("[3] Informar Tipo de cliente de la lista")
    print("[4] Salir")

if __name__== "__main__":
    menu()
    opcion = int(input("Ingrese una opcion [1-4]: "))
    while opcion != 4:
        if opcion == 1:
            pedro = Locales("Pedro", "Martínez", "pedro@example.com", "clave1234", "321 Calle Tranquila", "555-345-6789")
            maria = Locales("María", "García", "maria@example.com", "contraseña456", "456 Avenida Central", "555-987-6543")
            diego = Nacionales("Diego", "Sánchez", "diego@example.com", "secreto9876", "789 Avenida Porteña", "555-678-9012", "Buenos Aires", "La Plata", 1900)
            carlos = Locales("Carlos", "Rodríguez", "carlos@example.com", "clave789", "789 Calle Secundaria", "555-789-0123")
            elena = Nacionales("Elena", "González", "elena@example.com", "clave5678", "456 Calle Cordobesa", "555-567-8901", "Córdoba", "Villa María", 5900)
            laura = Nacionales("Laura", "Fernández", "laura@example.com", "contraseña5432", "321 Calle Mendocina", "555-789-0123", "Mendoza", "San Rafael", 5600)
            juan = Locales("Juan", "Pérez", "juan@example.com", "secreto123", "123 Calle Principal", "555-123-4567")
            carolina = Nacionales("Carolina", "Rodríguez", "carolina@example.com", "secreto1357", "654 Calle Salteña", "555-234-5678", "Salta", "Salta", 4400)
            andres = Nacionales("Andrés", "Pérez", "andres@example.com", "clave2468", "987 Avenida Tucumana", "555-890-1234", "Tucumán", "San Miguel de Tucumán", 4000)
            ana = Locales("Ana", "López", "ana@example.com", "secreto987", "987 Avenida Principal", "555-234-5678")
            
            lista.agregarCliente(pedro)
            lista.agregarCliente(carolina)
            lista.agregarCliente(maria)
            lista.agregarCliente(ana)
            lista.agregarCliente(elena)
            lista.agregarCliente(diego)
            lista.agregarCliente(juan)
            lista.agregarCliente(andres)
            lista.agregarCliente(laura)
            lista.agregarCliente(carlos)
            lista.imprimirLista()
        elif opcion == 2:
            lista.listar_nacionales()
        elif opcion == 3:
            posicion = int(input("Ingrese una posicion de la lista: "))
            lista.informar_cliente(posicion)
        menu()
        opcion = int(input("Ingrese una opcion [1-4]: "))
