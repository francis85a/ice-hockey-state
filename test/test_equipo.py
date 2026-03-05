import pytest
from src.equipo import Equipo
from src.jugadora import Jugadora
from src.posicion import Posicion


def test_Equipo():
    ciudad = Equipo("Canada")
    ciudad.añadir_jugador(Jugadora(29, "Marie-Philip Poulin",  Posicion.CENTER, 1))
    print ("test comprobado,")
    print(str(ciudad))