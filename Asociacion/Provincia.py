class Provincia:
    __nombre : str
    __cantHabitantes: int
    __gobernador: object
    def __init__(self,nombre, cantHabitantes, gobernador = None):
        self.__nombre = nombre
        self.__cantHabitantes = cantHabitantes
        self.__gobernador= gobernador
    def getGobernador(self):
       return self.__gobernador
     
    def setGobernador(self, gobernador):
        self.__gobernador = gobernador
