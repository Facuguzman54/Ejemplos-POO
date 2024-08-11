class Edificio:
    __id: int
    __nombre:  str
    __direccion: str
    __nombreEmpreCons: str
    __cantPisos: int
    __cantDeptos: int
    __listaDeptos: list
    
    def __init__(self, id, nombre, direccion, nombreEmpreCons, cantPisos, cantDeptos):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__nombreEmpreCons = nombreEmpreCons
        self.__cantPisos = cantPisos
        self.__cantDeptos = cantDeptos
        self.__listaDeptos = []

    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre
    
    def set_nuevoDepto(self, unDepto):
        self.__listaDeptos.append(unDepto)

    def getDireccion(self):
        return self.__direccion

    def getNombreEmpreCons(self):
        return self.__nombreEmpreCons

    def getCantPisos(self):
        return self.__cantPisos

    def getCantDeptos(self):
        return self.__cantDeptos

    def informarDatosPropietarios(self):
        for depto in self.__listaDeptos:
            print(f"Departamento {depto.get__id()} - Propietario: {depto.get__nyaProp()}")

    def calcularSuperficieTotal(self):
        acum = 0
        for depto in self.__listaDeptos:
            acum += depto.get__supCubierta()
        return acum
    
    def informarPorcentaje(self, propietario):
        totalProp = 0
        for depto in self.__listaDeptos:
            if depto.get__nyaProp() == propietario:
                totalProp += depto.get__supCubierta()
        supTotal = self.calcularSuperficieTotal()
        porcentaje = (totalProp*100)/supTotal
        print(f"{propietario} tiene una superficie total de: {totalProp} mts^2 y un representa el {int(porcentaje)}% del edificio")