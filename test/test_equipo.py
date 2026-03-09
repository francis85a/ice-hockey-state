import pytest
from src.equipo import Equipo
from src.jugadora import Jugadora
from src.posicion import Posicion



def test_Equipo_listar_jugadores():
    ciudad = Equipo("Canada")
    ciudad.añadir_jugador(Jugadora(29, "Marie-Philip Poulin",  Posicion.CENTER))
    ciudad.añadir_jugador(Jugadora(19, "Brianne Jenner",       Posicion.CENTER))
    ciudad.añadir_jugador(Jugadora(10, "Sarah Fillier",        Posicion.CENTER))
    ciudad.añadir_jugador(Jugadora(24, "Natalie Spooner",      Posicion.LEFTWING))
    ciudad.añadir_jugador(Jugadora( 3, "Jocelyne Larocque",    Posicion.LEFT_DEFENSEMAN))
    ciudad.añadir_jugador(Jugadora(35, "Ann-Renée Desbiens",   Posicion.GOALIE))
    print ("test comprobado,")
    print(str(ciudad.listar_jugadores()))

def test_registrar_gol():

    ciudad = Equipo("Canada")
    ciudad.añadir_jugador(Jugadora(29, "Marie-Philip Poulin",  Posicion.CENTER))
    goleadora = ciudad.obtener_jugador(29)
    goleadora.registrar_gol()
    assert goleadora._goles == 1