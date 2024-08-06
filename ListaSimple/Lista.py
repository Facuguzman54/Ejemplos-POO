from Nodo import Nodo
class Lista:
    __comienzo: Nodo

    def __init__(self):
        self.__comienzo=None
    def agregarNodo(self, dato):
        nodo = Nodo(dato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
    def listarDatos(self):
        aux = self.__comienzo
        while aux!=None:
            print(aux.getDato())
            aux=aux.getSiguiente()
    def eliminarPorDNI(self, dni):
        aux=self.__comienzo
        encontrado = False
        if aux.getDato().getDNI()==dni:
            encontrado=True
            print('Encontrado:'+str(aux.getDato()))
            self.__comienzo = aux.getSiguiente()
            del aux
        else:
            ant = aux
            aux = aux.getSiguiente()
        while not encontrado and aux != None:
            if aux.getDato().getDNI()==dni:
                encontrado=True
            else:
                ant = aux
                aux=aux.getSiguiente()
        if encontrado:
            print('Encontrado:'+str(aux.getDato()))
            ant.setSiguiente(aux.getSiguiente())
        else:
            print('El DNI {}, no está en la lista'.format(dni))