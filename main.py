def main():
    print("⚓ Bienvenido a Hundir la flota ⚓")

    tablero_jugador = tablero()
    tablero_rival = tablero()

    barcos_jugador = generar_barcos_auto()
    barcos_rival = generar_barcos_auto()

    colocar_barcos_jugador(tablero_jugador, barcos_jugador)
    colocar_barcos_rival(tablero_rival, barcos_rival)

    print("🧭 Tablero del jugador:")
    print(tablero_jugador)
    print("\n🌊 Tablero del rival:")
    print(tablero_rival)
    print("\n" + "―" * 40)
    
    disparos_rival = set()

    while True:
        print("\n🧭 Tu tablero:")
        mostrar_tablero(tablero_jugador)
        print("🎯 Tablero del rival:")
        mostrar_tablero(tablero_rival, ocultar=True)

        print("\n--- Tu turno ---")
        disparar_jugador(tablero_rival)

        if not quedan_barcos(tablero_rival):
            print("\n🎉 ¡Has ganado! Hundiste toda la flota enemiga.")
            break

        print("\n--- Turno de la máquina ---")
        disparar_rival(tablero_jugador, disparos_rival)

        if not quedan_barcos(tablero_jugador):
            print("\n💀 La máquina ha hundido todos tus barcos. Fin del juego.")
            break

if __name__ == "__main__":
    main()