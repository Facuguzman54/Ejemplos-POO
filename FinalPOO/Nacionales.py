from Locales import Locales

class Nacionales(Locales):
    __provincia: str
    __localidad: str
    __codigoPostal: int
    def __init__(self, nombre, apellido, email, contrasenia, dirPostal, tel, provincia, localidad, codigoPostal):
        super().__init__(nombre, apellido, email, contrasenia, dirPostal, tel)
        self.__provincia = provincia
        self.__localidad = localidad
        self.__codigoPostal = codigoPostal
    def get_provincia(self):
        return self.__provincia
    def get_localidad(self):
        return self.__localidad
    def get_codigoPostal(self):
        return self.__codigoPostal
    
    def __str__(self) -> str:
        return f"Nombre: {self.get_nombre()}, Provincia: {self.__provincia}"
    