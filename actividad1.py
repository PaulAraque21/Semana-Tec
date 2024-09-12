from turtle import *
from freegames import vector

def line(start, end):
    print(f"Dibujando línea desde {start} hasta {end}")
    # Levantar el lápiz para moverse sin dibujar
    up()
    # Ir a la posición inicial
    goto(start.x, start.y)
    # Bajar el lápiz para empezar a dibujar
    down()
    # Dibujar una línea hacia la posición final
    goto(end.x, end.y)

def square(start, end):
    print(f"Dibujando cuadrado desde {start} hasta {end}")
    up()
    goto(start.x, start.y)
    down()
    # Empezar a rellenar la figura con color
    begin_fill()

    # Dibuja los 4 lados del cuadrado
    for count in range(4):
        # Mover hacia adelante la distancia especificada
        forward(end.x - start.x)
        # Girar a 90 grados a la izquierda para pintar el cuadrado
        left(90)

    # Rellenar el cuadrado
    end_fill()

def draw_circle(start, end):
    print(f"Dibujando círculo desde {start} hasta {end}")
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Calcular el radio del círculo según la distancia entre puntos
    radius = abs(end.x - start.x)
    # Dibujar el círculo con el radio calculado
    circle(radius)

    end_fill()

def rectangle(start, end):
    print(f"Dibujando rectángulo desde {start} hasta {end}")
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Dibujar los dos pares de lados de rectánngulo
    for count in range(2):
        # Lado largo del rectángulo
        forward(end.x - start.x)
        left(90)
        # Lado corto del rectángulo
        forward(end.y - start.y)
        left(90)

    end_fill()

def triangle(start, end):
    print(f"Dibujando triángulo desde {start} hasta {end}")
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Dibujar los tres lados del triángulo
    for count in range(3):
        forward(end.x - start.x)
        # Girar a 120 grados para hacer el triángulo equilátero
        left(120)

    end_fill()

def tap(x, y):
    print(f"Clic detectado en: {x}, {y}")
    start = state['start']

    # SI no hay punto de inicio guardado, se almacena las coordenadas actuales
    if start is None:
        state['start'] = vector(x, y)
    else:
        # Obtener la forma seleccionada
        shape = state['shape']
        # Definir el punto final del dibujo
        end = vector(x, y)
        # Dibujar la forma entre el punto inicial y final
        shape(start, end)
        # Resetear el punto inicial para el siguiente dibujo
        state['start'] = None

def store(key, value):
    # Guardar una nueva forma o estado en el diccionario
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
