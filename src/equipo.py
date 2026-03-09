from src.jugadora import Jugadora

class Equipo:
    def __init__(self, nombre : str):
        self._nombre = nombre
        self._jugadores: dict[int, Jugadora] = {}

    @property
    def nombre(self):
        return self._nombre

    def añadir_jugador(self,jugadora):
        if jugadora.dorsal in self._jugadores:
            raise ValueError(
                f"Ya existe un jugador con el dorsal {jugadora.dorsal} en {self._nombre}.")

        self._jugadores[jugadora.dorsal] = jugadora

    def listar_jugadores(self):
        print(self._jugadores)

    def obtener_jugador(self,dorsal):
        if dorsal not in self._jugadores:
            raise ValueError(
                f"No existe un jugador con el dorsal {dorsal} en {self._nombre}.")
        return self._jugadores[dorsal]
    
    def jugadores_activos(self):
        activas = []
        for jugadora in self._jugadores.values():
            if jugadora.es_activo:
                activas.append(jugadora)
        return activas
    
    def total_goles(self):
        jugadoras= list(self._jugadores.values())
        total = 0
        for jugadora in jugadoras:
            total += jugadora._goles
        return total