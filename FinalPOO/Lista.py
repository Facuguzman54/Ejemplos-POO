from Nodo import Nodo
from Nacionales import Nacionales
class Lista:
    __comienzo: Nodo
    def __init__(self):
        self.__comienzo = None
    
    def agregarCliente(self, cliente):
        nuevo = Nodo(cliente)
        if self.__comienzo == None:
            self.__comienzo = nuevo
        else:
            aux = self.__comienzo
            while aux.get_siguiente()!=None:
                aux = aux.get_siguiente()
            aux.set_siguiente(nuevo)
    
    def imprimirLista(self):
        aux = self.__comienzo
        while aux:
            cliente = aux.get_dato()
            print(cliente)
            aux = aux.get_siguiente()
    
    def listar_nacionales(self):
        aux = self.__comienzo
        while aux:
            cliente = aux.get_dato()
            if isinstance(cliente, Nacionales):
                print(cliente)
            aux = aux.get_siguiente()
    
    def informar_cliente(self, posicion):
        i= 0
        aux = self.__comienzo
        while aux and i < posicion-1:
            aux = aux.get_siguiente()
            i+=1
            
        cliente = aux.get_dato()
        if isinstance(cliente, Nacionales):
            print(f"En la posicion [{posicion}], se encuentra un cliente Nacional")
        else:    
            print(f"En la posicion [{posicion}], se encuentra un cliente Local")

