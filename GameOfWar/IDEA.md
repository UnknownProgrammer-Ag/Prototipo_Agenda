
# BASE

Usando de base la estructura de War.py adaptar la idea de battle Royale como un Game of Life de Conway pero con la guerra.

# ELEMENTOS

Los elementos principales del juego serán las unidades (soldados, tanques, buques) representados respectivamente por " ¡ , # , % ".
Existiran en un tablero, donde se irán moviendo de manera aleatoria y entrarán en combate hasta que solo quede un individuo.

# MEDIOS

Usaré python, el framework de interfaz de terminal TEXTUAL y Colorama para dar color a los objetos.

# FÓRMULAS

La creación de unidades será pseudo-aleatoria, con un sistema de pesos dando prioridad a soldados, seguido de tanques y buques en un nivel menor.
Los escudos para balancear su capacidad tendrá una rareza del 40%, con un valor fijo de protección del 65% del daño.
Un disparo es una reducción de 1 pts de vida absoluto, con un cálculo de substracción del daño del escudo.
Las unidades se moverán en una cuadrícula (tamaño a definir), eligiendo a sus oponentes en las casillas adyacentes, solo permitiendo un combate entre sí.
