"""
Actividad 6: Juego del Packman

Equipo 9:
Christopher Gabriel Pedraza Pohlenz A01177767
Kevin Susej Garza Aragón A00833985
Eugenia Ruiz Velasco Olvera A01177887
"""

# Se importan las librerías de random, turtle, string y freegames
from random import *
from turtle import *
import string

from freegames import path

# Guarda la imagen en una variable
car = path('car.gif')

# Obtiene las letras mayúsculas y minúsculas y las convierte en listas
letras_minus = string.ascii_lowercase
alfabeto_minus = list(letras_minus)
letras_mayus = string.ascii_uppercase
alfabeto_mayus = list(letras_mayus)

# Concatena las letras minúsculas y parte de las mayúsculas
letras = alfabeto_minus + alfabeto_mayus[0:6]
# Duplica las letras
tiles = letras * 2

# Diccionario del estado de las posiciones del tablero
state = {'mark': None}
# Hacer una lista de 64 posiciones con todos los True
hide = [True] * 64

# Inicializa la variable globar de los clicks que se han dado
taps = 0


# Función que dibuja un cuadrado blanco con orilla negra en las posiciones x y y
def square(x, y):
    # Deja de dibujar
    up()
    # Mueve el cursor
    goto(x, y)
    # Comienza a dibujar
    down()
    color('black', 'white')
    begin_fill()
    # Hacer el cuadro de fondo
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


# Función que determina la posición 
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


# Función que determina tamaño y posición de los cuadritos
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


# Función que abre y cierra los cuadritos con el click
def tap(x, y):

    # Agrega 1 a los clicks e imprime
    global taps
    taps += 1
    print("Taps:", taps)
    
    # Obtiene la posición del tablero y su valor
    spot = index(x, y)
    mark = state['mark']

    # Si no se encuentra el par
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    # Si se encuentra el par
    else:
        # Se revela la imagen
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

        # Verificar si existe un cuadro sin descubrir
        for i in range(64):
            if hide[i] != False:
                return
        
        print("Victoria!")


# Función que dibuja del carro y la tipografía de las letras
def draw():
    # Elimina los dibujos
    clear()
    # Se mueve al origen
    goto(0, 0)
    # Pegar la imagen en la posición de la tortuga
    shape(car)
    stamp()

    # Volver a dibujar los cuadritos que no estén descubiertos
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    # Se posicionan los valores
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal', ), align="center")

    # Actualizar la pantalla de la tortuga
    update()
     # Llama a la función move, cada 100 milisegundos
    ontimer(draw, 100)

# Ordena aleatoriamente el tablero
shuffle(tiles)
# Establecer el ancho, largo, y posición inicial en x y y
setup(420, 420, 370, 0)
# Agrega la imagen del carro
addshape(car)
# Esconder el cursor, la tortuga
hideturtle()
# Elimina la animación de la tortuga
tracer(False)
# Al haber un click en la pantalla, se llama a esta función, pasando las coordenadas del click
onscreenclick(tap)
# Llama a la función draw
draw()
# Comienza el ciclo de eventos
done()
