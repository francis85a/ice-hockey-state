from src.equipo import Equipo
from src.jugadora import Jugadora
from src.posicion import Posicion

# ---------------------------------------------------------------------------
# Función auxiliar: detecta superioridad numérica (Power Play)
# ---------------------------------------------------------------------------

def es_power_play(equipo_atacante: Equipo, equipo_rival: Equipo) -> bool:
    """Devuelve True si el equipo atacante tiene más jugadores activos que el rival."""
    return len(equipo_atacante.jugadores_activos()) > len(equipo_rival.jugadores_activos())


def mostrar_marcador(marcador: dict[str, int], equipo_izq: Equipo, equipo_der: Equipo) -> str:
    """Devuelve la cadena formateada del marcador."""
    return (
        f"{equipo_izq.nombre} {marcador[equipo_izq.nombre]} "
        f"- {marcador[equipo_der.nombre]} {equipo_der.nombre}"
    )

def main() -> None:

    # -----------------------------------------------------------------------
    # Creación del roster — Equipo Canada
    # -----------------------------------------------------------------------
    canada = Equipo("Canada")

    canada.añadir_jugador(Jugadora(29, "Marie-Philip Poulin",  Posicion.CENTER ))
    canada.añadir_jugador(Jugadora(19, "Brianne Jenner",       Posicion.CENTER ))
    canada.añadir_jugador(Jugadora(10, "Sarah Fillier",        Posicion.CENTER))
    canada.añadir_jugador(Jugadora(24, "Natalie Spooner",      Posicion.LEFTWING))
    canada.añadir_jugador(Jugadora( 3, "Jocelyne Larocque",    Posicion.LEFT_DEFENSEMAN))
    canada.añadir_jugador(Jugadora(35, "Ann-Renée Desbiens",   Posicion.GOALIE))

    canada.listar_jugadores()

    usa = Equipo("USA")

    usa.añadir_jugador(Jugadora(21, "Hilary Knight",           Posicion.RIGHTWING))
    usa.añadir_jugador(Jugadora(28, "Amanda Kessel",           Posicion.CENTER))
    usa.añadir_jugador(Jugadora(26, "Kendall Coyne Schofield", Posicion.CENTER))
    usa.añadir_jugador(Jugadora(25, "Alex Carpenter",          Posicion.RIGHTWING))
    usa.añadir_jugador(Jugadora( 5, "Megan Keller",            Posicion.LEFT_DEFENSEMAN))
    usa.añadir_jugador(Jugadora( 1, "Alex Cavallini",          Posicion.GOALIE))

    usa.listar_jugadores()

    ## Marcador del partido (el valor no puede ser negativo)
    #marcador: dict[str, int] = {usa.nombre: 0, canada.nombre: 0}
#
    # # -----------------------------------------------------------------------
    ## Historia de usuario 1 — Gol de Canada en situación normal
    ## -----------------------------------------------------------------------
    #goleadora = canada.obtener_jugador(29)   # Marie-Philip Poulin
    #asistente = canada.obtener_jugador(19)   # Brianne Jenner
#
    #goleadora.registrar_gol()
    #print(f"Registrando gol para: {goleadora.nombre} y asistencia para {asistente.nombre}.")
    #print(goleadora)
 # M#arcador del partido (el valor no puede ser negativo)
    #marcador: dict[str, int] = {usa.nombre: 0, canada.nombre: 0}
#
    # # -----------------------------------------------------------------------
    ## Historia de usuario 1 — Gol de Canada en situación normal
    ## -----------------------------------------------------------------------
    #goleadora = canada.obtener_jugador(29)   # Marie-Philip Poulin
    #asistente = canada.obtener_jugador(19)   # Brianne Jenner
#
    #goleadora.registrar_gol()
    #print(f"Registrando gol para: {goleadora.nombre} y asistencia para {asistente.nombre}.")
    #print(goleadora)
#
if __name__ == "__main__":
    main()
