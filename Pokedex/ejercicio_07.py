def busqueda_lineal(pokemones, campo, valor):
    if campo not in ("nombre", "tipo", "nro"):
        raise ValueError(f"Campo invalido: {campo}")
    coincidencias = []
    for p in pokemones:
        if campo == "nombre":
            ok = p.nombre == valor
        elif campo == "tipo":
            ok = p.tipo1 == valor or p.tipo2 == valor
        else:
            ok = p.id == valor
        if ok:
            coincidencias.append(p)
    return coincidencias


def busqueda_binaria(pokemones, campo, valor):
    if campo not in ("nombre", "nro"):
        raise ValueError(f"Campo invalido: {campo}")
    izq = 0
    der = len(pokemones) - 1
    while izq <= der:
        medio = (izq + der) // 2
        p = pokemones[medio]
        clave = p.nombre if campo == "nombre" else p.id
        if clave == valor:
            return p
        if clave < valor:
            izq = medio + 1
        else:
            der = medio - 1
    return None


# TEORIA
# No: la binaria descarta la mitad de la lista suponiendo que esta ordenada por
# ese mismo campo; si esta ordenada por ataque, los nombres estan en cualquier
# orden y puede descartar la mitad donde estaba el nombre buscado.