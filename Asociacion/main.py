from Gobernador import Gobernador
from Provincia import Provincia
if __name__ == "__main__":
    cordoba = Provincia("Córdoba", 3000525)
    san_juan = Provincia("San Juan", 850000)
    mendoza = Provincia("Mendoza", 14000525)
    
    gobernador1 = Gobernador("12345678", "Juan Pérez", cordoba)
    gobernador2 = Gobernador("98765432", "María González", san_juan)
    gobernador3 = Gobernador("56789012", "Carlos Rodríguez", mendoza)

    cordoba.setGobernador(gobernador1)
    san_juan.setGobernador(gobernador2) 
    mendoza.setGobernador(gobernador3) 



