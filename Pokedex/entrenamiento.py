def subirAtaque(pokemon):
    incremento = 10
    pokemon.ataque += incremento
    print(f"El ataque de {pokemon.nombre} subió a {pokemon.ataque}.")

def subirDefensa(pokemon):
    incremento = 10
    pokemon.defensa += incremento
    print(f"La defensa de {pokemon.nombre} subió a {pokemon.defensa}.")

def subirVida(pokemon):
    incremento = 20
    pokemon.vida += incremento
    print(f"La vida de {pokemon.nombre} subió a {pokemon.vida}.")
