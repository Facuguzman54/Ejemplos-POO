class Departamento:
    __id : str
    __nyaProp: str
    __numPiso: int
    __numDepto: int
    __cantHabitaciones: int
    __cantBanios: int
    __supCubierta: float
    def __init__(self, id, nyaProp, numPiso, numDepto, cantHabitaciones, cantBanios, supCubierta):
        self.__id = id
        self.__nyaProp = nyaProp
        self.__numPiso = numPiso
        self.__numDepto = numDepto
        self.__cantHabitaciones = cantHabitaciones
        self.__cantBanios = cantBanios 
        self.__supCubierta = supCubierta

    def get__id(self):
        return self.__id

    def get__nyaProp(self):
        return self.__nyaProp

    def get__numPiso(self):
        return self.__numPiso

    def get__numDepto(self):
        return self.__numDepto

    def get__cantHabitaciones(self):
        return self.__cantHabitaciones
    
    def get__cantBanios(self):
        return self.__cantBanios

    def get__supCubierta(self):
        return self.__supCubierta