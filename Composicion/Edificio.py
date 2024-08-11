class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __nombreEmpresa: str
    __cantPisos: int
    __cantDepartamentos: int
    __Departamentos: list

    def __init__(self,id, nombre, direccion, nombreEmpresa, cantPisos, cantDepartamentos):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__nombreEmpresa = nombreEmpresa
        self.__cantPisos = cantPisos
        self.__cantDepartamentos = cantDepartamentos
        self.__Departamentos = []
    def get__Departamentos(self):
        return self.__Departamentos
    def set__Departamentos(self, departamento):
        self.__Departamentos.append(departamento)
    
    def __str__(self):
        return f'{self.__nombre}, Direccion: {self.__direccion}, Empresa Constructora: {self.__nombreEmpresa}'