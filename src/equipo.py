class Equipo:
    def __init__(self, nombre : str):
        self._nombre = nombre
        self._jugadores = []

    @property
    def nombre(self, nombre):
        self.nombre = nombre

    @property
    def ciudad(self,ciudad):
        self.ciudad = ciudad

    def añadir_jugador(self,jugadora):

        self._jugadores.append(jugadora)
    
        
    def listar_jugadores(self):
        print(self._jugadores)

    def obtener_jugador(self,dorsal):
        self.dorsal = dorsal

    def jugadores_activos(self):
        list.self._jugadores