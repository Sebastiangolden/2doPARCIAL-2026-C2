from ejercicio_02 import Pokedex, PokemonNoEncontrado


def descendientes(origen_id, pokedex, aristas):
    # Falla si el origen no esta en la Pokedex.
    pokedex.obtener(origen_id)
    resultado = []
    for origen, destino in aristas:
        if origen == origen_id:
            # Falla si el destino no esta en la Pokedex.
            pokedex.obtener(destino)
            resultado.append(destino)
            resultado.extend(descendientes(destino, pokedex, aristas))
    # Caso base: sin destinos el for no agrega nada y devuelve [].
    return resultado


# TEORIA
# Traza de descendientes(4) con aristas (4, 5) y (5, 6):
#   1) descendientes(4): encuentra (4, 5), agrega 5 y llama a descendientes(5)
#   2) descendientes(5): encuentra (5, 6), agrega 6 y llama a descendientes(6)
#   3) descendientes(6): no hay destinos -> caso base, devuelve []
# Luego vuelve: el llamado 2 devuelve [6] y el llamado 1 devuelve [5, 6].