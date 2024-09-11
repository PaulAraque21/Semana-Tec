from turtle import *
from random import randrange, choice
from freegames import square, vector

# Colores posibles para la serpiente y la comida
colors = ['blue', 'green', 'black', 'purple', 'orange']

# Se escogen colores random asegurando que sean diferentes el de la serpiente y la comida
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    "Función para mover la comida cada frame"
    move_direction = choice([vector(3, 0), vector(-3, 0), vector(0, 3), vector(0, -3)])
    new_food_position = food + move_direction

    # Solo mover la comida si la nueva posición no se sale del cuadro
    if inside(new_food_position):
        food.move(move_direction)

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # CPara saber si es que la serpiente se puede comer la comida, que no tenga que coincidir exactamente solo con tocarla
    if abs(head.x - food.x) < 10 and abs(head.y - food.y) < 10:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # Mover la comida de manera aleatoria en cada movimiento
    move_food()
    clear()

    # Dibujar la serpiente con el color seleccionado
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Dibujar la comida con el color seleccionado
    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()