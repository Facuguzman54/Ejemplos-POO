class Locales:
    __nombre: str
    __apellido:str
    __email: str
    __contrasenia: str
    __dirPostal: str
    __telefono: str
    def __init__(self,nombre, apellido, email, contrasenia, dirPostal, tel):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia
        self.__dirPostal = dirPostal
        self.__telefono = tel
 
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido

    def get_email(self):
        return self.__email

    def get_contrasenia(self):
        return self.__contrasenia
    
    def get_dir_postal(self):
        return self.__dirPostal

    def get_telefono(self):
        return self.__telefono
    
    def __str__(self) -> str:
        return f'{self.__nombre} {self.__apellido} {self.__dirPostal}'