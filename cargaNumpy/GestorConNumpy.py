import numpy as np
from Miembro import Miembro
import csv
class gestorMiembros():
    __cantidad: int
    __dimension: int
    __incremento: int
    __lista: np.ndarray
    def __init__(self, dimension =0, incremento=1):
        self.__lista= np.empty(dimension, dtype=Miembro)
        self.__cantidad = 0
        self.__incremento = incremento
        self.__dimension = dimension 

    def agregarMiembro(self, nuevo):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__lista.resize(self.__dimension)
            self.__lista[self.__cantidad]= nuevo
            self.__cantidad += self.__incremento
    
    def cargarVisualizaciones(self):
        archivo = open("Visualizaciones.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        c= 0
        for fila in reader:
            identificador, apellidoYNombre, mail = fila
            unMiembro = Miembro(identificador, apellidoYNombre, mail)
            self.agregarMiembro(unMiembro)
            c+=1
        print(f"{c} Miembros cargados")