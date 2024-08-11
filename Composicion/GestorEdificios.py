from Departamento import Departamento
from Edificio import Edificio
import csv

class GestorEdificios:
    __listaEdificios: list

    def __init__(self):
        self.__listaEdificios = []
        self.cargarEdificios()
    
    def get__listaEdificios(self):
        return self.__listaEdificios
    
    def get__edificioNorte(self):
        return self.__listaEdificios[0]
    def get__edificioSur(self):
        return self.__listaEdificios[1]

    def cargarEdificios(self):
        #EDIFICIO NORTE
        archivo = open("EdificioNorte.csv")
        reader = csv.reader(archivo, delimiter=";")
        self.cargarArchivo(archivo, reader)

        #EDIFICIO SUR
        archivo = open("EdificioSur.csv")
        reader = csv.reader(archivo, delimiter=";")
        self.cargarArchivo(archivo, reader)

    def cargarArchivo(self, archivo, reader):
        bandera = True
        for fila in reader:
            if bandera:
                id, nombre, direccion, nombreEmpresa, cantPisos, cantDepartamentos = fila
                UnEdificio = Edificio(id, nombre, direccion, nombreEmpresa, cantPisos, cantDepartamentos)
                self.__listaEdificios.append(UnEdificio)
                bandera = not bandera
            else:
                id, nya, numPiso, numDepartamento, cantHabitaciones, cantBanios, supCubierta = fila
                UnDepartamento = Departamento(int(id), nya, int(numPiso), int(numDepartamento), int(cantHabitaciones), int(cantBanios), float(supCubierta))
                UnEdificio.set__Departamentos(UnDepartamento)
        
    def mostrarEdificio(self, nombre):
        
        if nombre == 'Norte':
            edificio = self.get__edificioNorte()
        else:
            edificio = self.get__edificioSur()

        for departamento in edificio.get__Departamentos():
            print(departamento)
    
    def calcularSuperficie(self, nombre):
        total = 0
        if nombre == 'Norte':
            edificio = self.get__edificioNorte()
        else:
            edificio = self.get__edificioSur()

        for departamento in edificio.get__Departamentos():
            total += departamento.get__supCubierta()
        print(f"El total de superficio cubierta del Edificio {nombre} es: {total}m2")

    def porcentajeSuperficie(self, nombre, i=0):
        totalEdificio = 0
        total = 0
        edificio = self.__listaEdificios[i]
        for departamento in edificio.get__Departamentos():
            totalEdificio += departamento.get__supCubierta()
            if nombre == departamento.get__nya():
                total += departamento.get__supCubierta()
        porcentaje = (total * 100)/totalEdificio
        if total == 0:
            print("El nombre ingresado no vive en este edificio")
        else:
            print(f"La superficie total que cubre {nombre} es el {porcentaje:.2f}%")
        i+=1
        if i < 2: self.porcentajeSuperficie(nombre,i)