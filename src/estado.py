from src.jugadora import Jugadora

class Estado_jugador:
    def registrar_gol(self, jugador: Jugadora):
        pass

    def registrar_asistencia(self, jugador: Jugadora):
        pass

class Jugador_activo(Estado_jugador):
    def registrar_gol(self, jugador: Jugadora):
        jugador._goles += 1
    def registrar_asistencia(self, jugador: Jugadora):
        jugador._asistencias += 1

class Jugador_inactivo(Estado_jugador):
    def registrar_gol(self, jugador: Jugadora):
        print(f"El jugador {jugador.nombre} está inactivo, no se puede registrar el gol.") 
    
    def registrar_asistencia(self, jugador: Jugadora):
        print(f"El jugador {jugador.nombre} está inactivo, no se puede registrar la asistencia.")