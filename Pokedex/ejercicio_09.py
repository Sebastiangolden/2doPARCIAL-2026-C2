import csv

from ejercicio_01 import Pokemon
from ejercicio_02 import Pokedex

ENCABEZADO = ["id", "nombre", "tipo1", "tipo2", "hp", "ataque", "defensa",
              "velocidad", "generacion"]


class ArchivoInvalidoError(Exception):
    pass


def guardar_csv(ruta, pokedex):
    with open(ruta, "w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(ENCABEZADO)
        for p in pokedex.listar():
            escritor.writerow([p.id, p.nombre, p.tipo1, p.tipo2, p.hp,
                               p.ataque, p.defensa, p.velocidad, p.generacion])


def cargar_csv(ruta):
    pokedex = Pokedex()
    with open(ruta, "r", encoding="utf-8", newline="") as f:
        lector = csv.reader(f)
        try:
            cabecera = next(lector)
        except StopIteration:
            raise ArchivoInvalidoError("El archivo no tiene encabezado")
        if cabecera != ENCABEZADO:
            raise ArchivoInvalidoError("Encabezado invalido")
        for fila in lector:
            if not fila:
                continue
            if len(fila) != 9:
                raise ArchivoInvalidoError(f"Fila con {len(fila)} columnas")
            try:
                pokemon = Pokemon(int(fila[0]), fila[1], fila[2], fila[3],
                                  int(fila[4]), int(fila[5]), int(fila[6]),
                                  int(fila[7]), int(fila[8]))
            except ValueError:
                raise ArchivoInvalidoError("Numero no convertible")
            pokedex.agregar(pokemon)
    return pokedex


# TEORIA
# Si, hace falta leer los anteriores: cada linea tiene largo variable, asi que
# no se puede calcular donde empieza la numero 10 sin recorrer las otras.
# El acceso es secuencial.