from src.jugadora import Jugadora

class Equipo:
    def __init__(self, nombre : str):
        self._nombre = nombre
        self._jugadores: dict[int, Jugadora] = {}

    @property
    def nombre(self):
        return self._nombre

    def añadir_jugador(self,jugadora):

        self._jugadores[jugadora.dorsal] = jugadora

    def listar_jugadores(self):
        print(self._jugadores)

    def obtener_jugador(self,dorsal):
        self.dorsal = dorsal

    def jugadores_activos(self):
        list.self._jugadores
