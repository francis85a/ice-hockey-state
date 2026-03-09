from src.posicion import Posicion
from src.estado import Estado_jugador, Jugador_activo, Jugador_inactivo
class Jugadora:

    def __init__(self, dorsal:int, nombre:str, posicion: Posicion):
        self._dorsal = dorsal
        self._nombre = nombre
        self.posicion: Posicion = posicion
        self._goles = 0
        self._asistencias = 0
        self._estado: Estado_jugador = Jugador_activo()

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
        return isinstance(self._estado, Jugador_activo)
    
    def registrar_gol(self):
        self._estado.registrar_gol(self)
    
    def registrar_asistencia(self):
        self._estado.registrar_asistencia(self)
        
    def sancionar(self, minutos: int):
        self._estado = Jugador_inactivo()
        self._minutos_sancion = minutos


    def liberar(self):
        self._estado = Jugador_activo()

    def __str__(self):
        estado_str = "Activo" if self.es_activo else "Inactivo"
        return (
            f"{self._dorsal:>2}{self._nombre:<30}"
            f"{self.posicion.value:<18}"
            f"G:{self._goles} A :{self._asistencias} {estado_str}"
        )
    def __repr__(self):
        return f"jugadora({self._dorsal}, '{self._nombre}', {self.posicion})"