from capturados import agregar_capturado

def simular_combate(pokemon_usuario, pokemones_enemigos):
    import random
    enemigo = random.choice(pokemones_enemigos)
    print(f"¡Un {enemigo.nombre} salvaje apareció!")
    while pokemon_usuario.vida > 0 and enemigo.vida > 0:
        print("\nOpciones de ataque:")
        print("1. Ataque básico")
        print("2. Ataque especial")
        opcion = int(input("Elige tu ataque: "))
        if opcion == 1:
            pokemon_usuario.atacar(enemigo)
        else:
            pokemon_usuario.atacar(enemigo)  # Asume que el ataque especial es el mismo

        if enemigo.vida > 0:
            enemigo.atacar(pokemon_usuario)

    if pokemon_usuario.vida > 0:
        print(f"¡Has derrotado a {enemigo.nombre}!")
        captura = input("¿Quieres capturar a este Pokémon? (s/n): ").lower()
        if captura == 's':
            enemigo.atrapado = True
            agregar_capturado(enemigo)
    else:
        print(f"¡{pokemon_usuario.nombre} ha sido derrotado!")
