class Departamento:
    __id = int
    __nya = str
    __numPiso = int
    __numDepartamento = int
    __cantHabitaciones = int
    __cantBanios = int
    __supCubierta = float

    def __init__(self, id, nya, numPiso, numDepartamento, cantHabitaciones, cantBanios, supCubierta):
        self.__id = id
        self.__nya = nya
        self.__numPiso = numPiso
        self.__numDepartamento = numDepartamento
        self.__cantHabitaciones = cantHabitaciones
        self.__cantBanios = cantBanios
        self.__supCubierta = supCubierta

    def get__supCubierta(self):
        return self.__supCubierta
    def get__nya(self):
        return self.__nya

    def __str__(self) -> str:
        return f'Inquilino: {self.__nya}, Piso Numero: {self.__numPiso}, Departamento Numero: {self.__numDepartamento}'