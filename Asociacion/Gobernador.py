class Gobernador:
    __dni : str
    __nombreApellido: str
    __provincia: object
    def __init__(self,dni, nombreApellido, provincia = None):
        self.__dni = dni
        self.__nombreApellido = nombreApellido
        self.__provincia= provincia
    def getProvincia(self):
       return self.__provincia 
    def setProvincia(self, provincia):
        self.__provincia = provincia