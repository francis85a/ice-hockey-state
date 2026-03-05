# Francisco Pérez Cid (github:francis85a)
### Enlace al repo
https://github.com/francis85a/ice-hockey-state

## 1. Instalacion y ejecucion

Instalar entorno virtual

```python3 venv .venv```

Instalar dependencias

```python3 install requirements.txt ```

Ejecutar programa

```python3 ice_state.py```

## 2. Diagrama de Clases

```text
  ┌──────────────────────┐              ┌──────────────────────────────────────────────-┐
  │                      │              │                   «abstract»                  │
  │        Posicion      │              │                 EstadoJugador                 │
  ├──────────────────────┤              ├──────────────────────────────────────────────-┤
  │  CENTER              │              │ + registrar_gol(jugadora: Jugadora)«abstract» │
  │  LEFTWING            │              │ + registrar_asistencia(j: Jugadora) «abstract»│
  │  RIGHTWING           │              └─────────────────────────▲--──────────────────-┘
  │  LEFT_DEFENSEMAN     │                                        │  is a  
  │  RIGHT_DEFENSEMAN    │                          ┌─────────────┴─────────────┐
  │  GOALIE              │                          |                           |
  └──────────────────────┘                 ┌─────────────────────────┐  ┌───────────────────────────┐
             ▲                             │     JugadorActivo       │  │    JugadorSancionado      │
             |                             ├─────────────────────────┤  ├───────────────────────────┤
  ┌──────────────────────────────────────┐ │ + registrar_gol()       │  │ + registrar_gol()         │
  │               Jugadora               │ │ + registrar_asistencia()│  │ + registrar_asistencia()  │
  ├──────────────────────────────────────┤ └─────────────────────────┘  └───────────────────────────┘
  │ - dorsal      : int                  │
  │ - nombre      : str                  │
  │ - posicion    : Posicion             │
  │ - goles       : int                  │
  │ - asistencias : int                  │
  │ - estado      : EstadoJugador        ├─── estado ────────▶ EstadoJugador
  ├──────────────────────────────────────┤
  │ + dorsal       : int        {prop}   │
  │ + nombre       : str        {prop}   │
  │ + posicion     : Posicion   {prop}   │
  │ + goles        : int        {prop}   │
  │ + asistencias  : int        {prop}   │
  │ + es_activo    : bool       {prop}   │
  ├──────────────────────────────────────┤
  │ + registrar_gol()                    │
  │ + registrar_asistencia()             │
  │ + sancionar(minutos: int)            │
  │ + liberar()                          │
  └──────────────────────────────────────┘
                     ▲
                1..* │
                     ◆
  ┌──────────────────────────────────────────┐
  │                  Equipo                  │
  ├──────────────────────────────────────────┤
  │ -  nombre    : str                       │
  │ -  ciudad    : str                       │
  │ -  jugadores : dict[int, Jugadora]       │
  ├──────────────────────────────────────────┤
  │ + nombre     : str              {prop}   │
  │ + ciudad     : str              {prop}   │
  │ + añadir_jugador(jugadora: Jugadora)     │
  │ + listar_jugadores()                     │
  │ + obtener_jugador(dorsal: int)           │
  │ + jugadores_activos() → list[Jugadora]   │
  │ + total_goles()                          │
  └──────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │                  Main                                                                                 │
  ├───────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ +  marcador : dict[str, int]                                                                          │
  ├───────────────────────────────────────────────────────────────────────────────────────────────────────|
  │ + mostrar_marcador(marcador: dict[str, int], equipo_izq: Equipo, equipo_der: Equipo) -> str:          │
  │ + es_power_play(equipo_atacante: Equipo, equipo_rival: Equipo) → bool                                 │
  └───────────────────────────────────────────────────────────────────────────────────────────────────────┘

  Notación
  ─────────────────────────────────────────────────────────────
  {prop}    atributo expuesto mediante @property (read-only)
```

---

## Comprobación con pytest y coverage

![alt text](img/image.png)
---
![alt text](img/image2.png)