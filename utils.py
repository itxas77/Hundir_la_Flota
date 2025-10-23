import numpy as np
import random
import time


def tablero():
    return np.full((10, 10), " ")

def generar_barcos_auto():
    esloras = [2, 2, 2, 3, 3, 4]
    barcos = []
    posiciones_ocupadas = set()
    for eslora in esloras:
        colocado = False # indica si se ha colocado con éxito
        intentos = 0 # cuantas veces hemos probado posiciones aleatorias (para evitar bucles infinitos)
        while not colocado and intentos < 500:
            intentos += 1
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            orientacion = random.choice(["H", "V"]) #aparte del número también elige si en horizontal o vertical
            if orientacion == "H":
                if columna + eslora <= 10: #para no salirse del tablero
                    candidate = [(fila, c) for c in range(columna, columna + eslora)]
                else:
                    continue #si se sale del tablero vuelve a intentarlo hasta 500 veces
            else: #si lo coloca en vertical
                if fila + eslora <= 10:
                    candidate = [(r, columna) for r in range(fila, fila + eslora)] 
                else:
                    continue
            if any(pos in posiciones_ocupadas for pos in candidate): #si la celda está ocupada continua con otro intento
                continue
            # si el candidato cumple las condiciones arriba, pasa a ser barco
            barcos.append(candidate)
            for pos in candidate:
                posiciones_ocupadas.add(pos) # cada posición del candidate se añade a posiciones_ocupadas.
            colocado = True #para salir del while y colocar el siguiente barco
        if not colocado:
            # en caso de fallo raro, reiniciar todo (estrategia simple)
            return generar_barcos_auto()
    return barcos


def colocar_barcos_jugador(tablero_jugador, barcos_jugador):
    for barco in barcos_jugador:
        for posicion in barco:
            tablero_jugador[posicion] = "O"
    return tablero_jugador

def colocar_barcos_rival(tablero_rival, barcos_rival):
    for barco in barcos_rival:
        for posicion in barco:
            tablero_rival[posicion] = "O"
    return tablero_rival

def mostrar_tablero(tablero_jugador, ocultar =False):
    simbolos = {
        " ": "🌊",  # agua sin disparar
        "O": "🚢",  # barco
        "X": "💥",  # tocado
        "#": "⚪",  # agua disparada
    }
    print("   " + "―" * 30)
    for i, fila in enumerate(tablero_jugador):
        fila_mostrada = []
        for x in fila:
            if ocultar and x == "O":
                fila_mostrada.append(simbolos[" "])
            else:
                fila_mostrada.append(simbolos.get(x, x))
        print(i, "|", *fila_mostrada)
    print("")


def disparar(tablero, fila, columna):
    if tablero[fila, columna] == "O":
        print("💥 ¡Tocado!")
        tablero[fila, columna] = "X"
    elif tablero[fila, columna] in ["X", "#"]:
        print("⚠️ Ya habías disparado aquí.")
    else:
        print("🌊 Agua!")
        tablero[fila, columna] = "#"
    return tablero


def quedan_barcos(tablero_jugador):
    return np.any(tablero_jugador == "O")

def disparar_jugador(tablero_rival):
    mostrar_tablero(tablero_rival, ocultar=True)
    while True:
        try:
            fila = int(input("Fila (0-9): "))
            columna = int(input("Columna (0-9): "))
            if 0 <= fila < 10 and 0 <= columna < 10:
                disparar(tablero_rival, fila, columna)
                break
            else:
                print("❌ Coordenadas fuera del rango.")
        except ValueError:
            print("❌ Introduce números válidos.")
    if tablero_rival[fila, columna] == "O":
        print("💥 ¡Tocado!")
        tablero_rival[fila, columna] = "X"
    elif tablero_rival[fila, columna] in ["X", "#"]:
        print("⚠️ Ya habías disparado aquí.")
    else:
        print("🌊 Agua.")
        tablero_rival[fila, columna] = "#"


def disparar_rival(tablero_jugador, disparos_previos):
    while True:
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        if (fila, columna) not in disparos_previos:
            disparos_previos.add((fila, columna))
            print(f"\n🎯 La máquina dispara a ({fila}, {columna})...")
            disparar(tablero_jugador, fila, columna)
            break