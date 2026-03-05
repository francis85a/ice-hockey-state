from src.equipo import Equipo

class Jugadora(Equipo):

    def __init__(self, dorsal:int, nombre:str, posicion, goles):
        self._dorsal = dorsal
        self._nombre = nombre
        self.Posicion = posicion
        self._goles = goles
    
    def registrar_gol(self, goles):
        self.goles = goles
        ACTIVA = True
        INACTIVA = False
        if Jugadora is ACTIVA:
            goles + 1
        else:
            INACTIVA