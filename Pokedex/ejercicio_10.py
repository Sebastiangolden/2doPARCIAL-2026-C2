import struct

from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex
from ejercicio_09 import ArchivoInvalidoError

FORMATO_ENCABEZADO = "<4scI"
FORMATO_REGISTRO = "<I20s12s12s4H"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)  # 9
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)      # 56
MAGIA = b"AYED"
TEMA = b"P"


def _empaquetar(p):
    # struct con "Ns" recorta o rellena con \0 al ancho del campo.
    return struct.pack(FORMATO_REGISTRO, p.id,
                       p.nombre.encode("utf-8"),
                       p.tipo1.encode("utf-8"),
                       p.tipo2.encode("utf-8"),
                       p.hp, p.ataque, p.defensa, p.velocidad)


def _texto(bytes_):
    return bytes_.rstrip(b"\0").decode("utf-8", errors="ignore")


def _leer_encabezado(f):
    datos = f.read(TAM_ENCABEZADO)
    if len(datos) < TAM_ENCABEZADO:
        raise ArchivoInvalidoError("Archivo mas corto que el encabezado")
    magia, _tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, datos)
    if magia != MAGIA:
        raise ArchivoInvalidoError("Magia invalida")
    return cantidad


def guardar_binario(ruta, pokedex):
    pokemones = pokedex.listar()
    with open(ruta, "wb") as f:
        f.write(struct.pack(FORMATO_ENCABEZADO, MAGIA, TEMA, len(pokemones)))
        for p in pokemones:
            f.write(_empaquetar(p))


def cargar_binario(ruta):
    pokedex = Pokedex()
    with open(ruta, "rb") as f:
        cantidad = _leer_encabezado(f)
        for _ in range(cantidad):
            datos = f.read(TAM_REGISTRO)
            if len(datos) < TAM_REGISTRO:
                raise ArchivoInvalidoError("Registro incompleto")
            id_, nombre, tipo1, tipo2, hp, ataque, defensa, vel = \
                struct.unpack(FORMATO_REGISTRO, datos)
            pokedex.agregar(Pokemon(id_, _texto(nombre), _texto(tipo1),
                                    _texto(tipo2), hp, ataque, defensa,
                                    vel, 1))
    return pokedex


def actualizar_registro(ruta, posicion, pokemon):
    with open(ruta, "r+b") as f:
        cantidad = _leer_encabezado(f)
        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError("Posicion fuera de rango")
        f.seek(TAM_ENCABEZADO + posicion * TAM_REGISTRO)
        f.write(_empaquetar(pokemon))


# TEORIA
# El tamaño fijo de cada registro (56 bytes), junto con el tamaño del
# encabezado (9 bytes): el registro `posicion` empieza en el byte
# 9 + posicion * 56.