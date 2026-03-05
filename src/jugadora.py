from src.posicion import Posicion

class Jugadora:

    def __init__(self, dorsal:int, nombre:str, posicion: Posicion):
        self._dorsal = dorsal
        self._nombre = nombre
        self.posicion: Posicion = posicion
        self._goles = 0
        self._asistencias = 0
        self._estado = "ACTIVA"

    @property
    def dorsal(self):
        return self._dorsal
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def goles(self):
        return self._goles
    
    @property
    def asistencias(self):
        return self._asistencias

    @property
    def es_activo(self):
        return self._estado == "ACTIVA"

    
    #def registrar_gol(self, goles):
    #    self.goles = goles
    #    ACTIVA = True
    #    INACTIVA = False
    #    if Jugadora is ACTIVA:
    #        goles + 1
    #    else:
    #        INACTIVA