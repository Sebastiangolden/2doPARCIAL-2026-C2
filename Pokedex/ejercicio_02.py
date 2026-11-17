from ejercicio_01 import Pokemon


class PokemonNoEncontrado(Exception):
    pass


class Pokedex:
    def __init__(self):
        self._pokemones = []

    def agregar(self, pokemon):
        for i, existente in enumerate(self._pokemones):
            if existente.id == pokemon.id:
                self._pokemones[i] = pokemon
                return
        self._pokemones.append(pokemon)

    def obtener(self, id):
        for pokemon in self._pokemones:
            if pokemon.id == id:
                return pokemon
        raise PokemonNoEncontrado(f"No existe el Pokemon con id {id}")

    def listar(self):
        return list(self._pokemones)

    def cantidad(self):
        return len(self._pokemones)

# TEORIA
# Quien llama no puede ignorar el error por descuido: si el id no esta, el
# programa se entera de inmediato, y no se confunde "no existe" (None) con un
# dato valido ni hay que chequear None despues de cada llamada.