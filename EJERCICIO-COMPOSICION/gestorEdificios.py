import csv

from Edificio import Edificio
from Departamento import Departamento

class gestorEdificios:
    __lista: list
    def __init__(self) -> None:
        self.__lista = []

    def cargarEdificios(self):
        archivo = open("EdificioNorte.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if "Edificio" in fila[1]:
                idEdificio, nombre, direccion, nombreEmpreCons, cantPisos, cantDeptos = fila
                xEdificio = Edificio(idEdificio, nombre, direccion, nombreEmpreCons, int(cantPisos), int(cantDeptos))
                self.__lista.append(xEdificio)
            else:
                idEdificio,idDepto, nyaProp, numPiso, numDepto, cantHabitaciones, cantBanios, supCubierta = fila
                xDepartamento = Departamento(idDepto, nyaProp, int(numPiso), int(numDepto), int(cantHabitaciones), int(cantBanios), float(supCubierta))
                xEdificio.set_nuevoDepto(xDepartamento)
    def mostrarDatosPropietarios(self, nombreEdificio):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.__lista):
            if self.__lista[i].getNombre() == nombreEdificio:
                encontrado = True
            else:
                i+=1
        if encontrado:
            self.__lista[i].informarDatosPropietarios()
        
    def mostrarSupTotalEdificio(self):
        for edificio in self.__lista:
            print(f"La superficie total del edificio, {edificio.getNombre()} es: {edificio.calcularSuperficieTotal()} mts^2")
    
    def superficieDelProp(self,propietario):
        for edificio in self.__lista:
            print(f"----Para {edificio.getNombre()}---")
            edificio.informarPorcentaje(propietario)