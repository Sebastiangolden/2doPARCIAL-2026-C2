class Pokemon:
    def __init__(self, id, nombre, tipo1, tipo2, hp, ataque, defensa,
                 velocidad, generacion):
        self.id = id
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    def __str__(self):
        if self.tipo2:
            return f"#{self.id} {self.nombre} ({self.tipo1}/{self.tipo2})"
        return f"#{self.id} {self.nombre} ({self.tipo1})"

    def __eq__(self, otro):
        return isinstance(otro, Pokemon) and self.id == otro.id

    def __hash__(self):
        return hash(self.id)


# TEORIA
# La identidad es el atributo `id`; el estado son nombre, tipos, hp, ataque,
# defensa, velocidad y generacion. No: la identidad no debe cambiar despues de
# construido el objeto, porque es lo que permite reconocerlo como el mismo.