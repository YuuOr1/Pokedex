from pokemon_clases import PokemonAgua, PokemonFuego, PokemonElectrico, PokemonHierba
from combate import simular_combate
from entrenamiento import subirAtaque, subirDefensa, subirVida
from capturados import mostrar_capturados

def interfaz_usuario():
    print("¡Bienvenido a tu Pokedex!")
    nombre_usuario = input("¿Cómo te llamas? ")
    print(f"Hola {nombre_usuario}, elige tu Pokémon inicial:")
    print("1. Agua\n2. Fuego\n3. Eléctrico\n4. Hierba")
    opcion = int(input("Selecciona (1-4): "))

    if opcion == 1:
        pokemon_usuario = PokemonAgua()
    elif opcion == 2:
        pokemon_usuario = PokemonFuego()
    elif opcion == 3:
        pokemon_usuario = PokemonElectrico()
    elif opcion == 4:
        pokemon_usuario = PokemonHierba()
    else:
        print("Opción inválida.")
        return

    pokemones_enemigos = [
        PokemonFuego("Charizard"),
        PokemonAgua("Blastoise"),
        PokemonElectrico("Raichu"),
        PokemonHierba("Venusaur")
    ]

    while True:
        print("\nOpciones:")
        print("1. Entrenar Pokémon")
        print("2. Mostrar Pokémon capturados")
        print("3. Simular combate")
        print("4. Salir")
        eleccion = int(input("¿Qué deseas hacer? "))

        if eleccion == 1:
            print("Entrenamiento:")
            print("1. Subir ataque\n2. Subir defensa\n3. Subir vida")
            ent_opcion = int(input("Selecciona: "))
            if ent_opcion == 1:
                subirAtaque(pokemon_usuario)
            elif ent_opcion == 2:
                subirDefensa(pokemon_usuario)
            elif ent_opcion == 3:
                subirVida(pokemon_usuario)
            else:
                print("Opción inválida.")
        elif eleccion == 2:
            mostrar_capturados()
        elif eleccion == 3:
            simular_combate(pokemon_usuario, pokemones_enemigos)
        elif eleccion == 4:
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    interfaz_usuario()
