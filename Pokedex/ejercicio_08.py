def _clave(pokemon, campo):
    if campo == "ataque":
        return pokemon.ataque
    if campo == "velocidad":
        return pokemon.velocidad
    if campo == "nro":
        return pokemon.id
    raise ValueError(f"Campo invalido: {campo}")


def ordenar_seleccion(pokemones, campo, descendente):
    n = len(pokemones)
    for i in range(n - 1):
        elegido = i
        for j in range(i + 1, n):
            a = _clave(pokemones[j], campo)
            b = _clave(pokemones[elegido], campo)
            if (a > b) if descendente else (a < b):
                elegido = j
        if elegido != i:
            pokemones[i], pokemones[elegido] = pokemones[elegido], pokemones[i]
    return pokemones


def ordenar_insercion(pokemones, campo, descendente):
    for i in range(1, len(pokemones)):
        actual = pokemones[i]
        k = _clave(actual, campo)
        j = i - 1
        while j >= 0:
            previo = _clave(pokemones[j], campo)
            # Comparacion estricta: los iguales no se cruzan (estable).
            if (previo < k) if descendente else (previo > k):
                pokemones[j + 1] = pokemones[j]
                j -= 1
            else:
                break
        pokemones[j + 1] = actual
    return pokemones


# TEORIA
# El estable es el de insercion. Un algoritmo es estable si los elementos con
# la misma clave conservan entre si el orden relativo que tenian antes de
# ordenar (la seleccion no lo es, porque su intercambio a distancia puede
# pasar un elemento por encima de otro con igual clave).