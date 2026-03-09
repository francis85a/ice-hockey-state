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

def test_registrar_asistencia():

    ciudad = Equipo("Canada")
    ciudad.añadir_jugador(Jugadora(29, "Marie-Philip Poulin",  Posicion.CENTER))
    asistente = ciudad.obtener_jugador(29)
    asistente.registrar_asistencia()
    assert asistente._asistencias == 1

def test_jugadora_activa():
    ciudad = Equipo("Canada")
    ciudad.añadir_jugador(Jugadora(29, "Marie-Philip Poulin",  Posicion.CENTER))
    jugadora = ciudad.obtener_jugador(29)
    assert jugadora.es_activo == True

def test_total_goles():
    ciudad = Equipo("Canada")
    ciudad.añadir_jugador(Jugadora(29, "Marie-Philip Poulin",  Posicion.CENTER))
    ciudad.añadir_jugador(Jugadora(19, "Brianne Jenner",       Posicion.CENTER))
    goleadora1 = ciudad.obtener_jugador(29)
    goleadora2 = ciudad.obtener_jugador(19)
    goleadora1.registrar_gol()
    goleadora2.registrar_gol()
    assert ciudad.total_goles() == 2