🧭 README.md — Hundir la Flota

# ⚓ Hundir la Flota (versión Python con emojis)

¡Bienvenido al clásico juego de **Hundir la flota** hecho en Python! 🚢💥  
Este proyecto implementa una versión jugable por consola donde el jugador se enfrenta a la máquina en una batalla naval por turnos.

---

## 🧩 Descripción general

El juego genera automáticamente los tableros del jugador y del rival, coloca los barcos de forma aleatoria y gestiona los turnos de disparo hasta que uno de los dos hunde toda la flota enemiga.

Se usan **emojis** para representar el estado visual del tablero:

| Símbolo | Significado         |
|----------|--------------------|
| 🌊       | Agua sin disparar  |
| 🚢       | Barco              |
| 💥       | Tocado             |
| ⚪       | Agua disparada     |

---

## 🗂️ Estructura del proyecto
📂 hundir_la_flota/
│
├── main.py # Contiene la función principal y el bucle del juego
├── utils.py # Funciones auxiliares (tableros, disparos, generación de barcos, etc.)
└── README.md # Este archivo

⚙️ Funciones principales
En utils.py

tablero(): crea un tablero vacío de 10x10.

generar_barcos_auto(): coloca automáticamente los barcos (esloras 2, 2, 2, 3, 3, 4).

colocar_barcos_jugador() y colocar_barcos_rival(): sitúan los barcos en los tableros.

mostrar_tablero(): imprime el tablero con emojis (con opción de ocultar barcos enemigos).

disparar(): gestiona el impacto o fallo en una coordenada.

disparar_jugador() y disparar_rival(): ejecutan los turnos de disparo.

quedan_barcos(): comprueba si aún quedan barcos a flote.

En main.py

main(): inicia el juego, muestra los tableros, alterna turnos y determina el ganador.

🧠 Lógica básica del juego

Se inicializan dos tableros (jugador y rival).

Se colocan barcos automáticamente en ambos.

El jugador y la máquina disparan por turnos.

Gana quien hunda todos los barcos del oponente primero.

🌈 Características adicionales

Interfaz visual con emojis.

Control de errores en la entrada de coordenadas.

Detección de disparos repetidos.

Comprobación automática de victoria/derrota.

Código limpio y modular.

💡 Mejoras futuras

Añadir un modo multijugador local o en red.

Guardar puntuaciones y estadísticas.

Crear una interfaz gráfica con tkinter o pygame.

Mejorar la IA del rival (actualmente dispara aleatoriamente).

👨‍💻 Autor

Proyecto desarrollado por Itxaso Campos
📅 Octubre 2025
🧭 Versión: 1.0
