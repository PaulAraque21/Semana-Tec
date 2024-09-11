from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None, 'taps': 0}  # Agregamos contador de taps
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark, hidden tiles, and count taps based on tap."
    state['taps'] += 1  # Contar el tap
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Detectar si todos los cuadros han sido destapados
    if all(not hidden for hidden in hide):
        print(f"¡Felicidades! Has descubierto todos los cuadros en {state['taps']} taps.")

def draw():
    "Draw image, tiles, and number of taps."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 15, y + 5)  # Ajustar para centrar el dígito
        color('black')
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    # Mostrar el número de taps
    up()
    goto(-180, 180)
    color('black')
    write(f"Taps: {state['taps']}", font=('Arial', 15, 'normal'))

    update()
    ontimer(draw, 100)

# Mezclamos los tiles
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
