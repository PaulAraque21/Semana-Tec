from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)  
speed = vector(0, 0)  
targets = []  

def tap(x, y):
    "Responder al toque en la pantalla."
    if not inside(ball):  
        ball.x = -199  
        ball.y = -199
        speed.x = (x + 200) / 15  # Aumenta la velocidad del disparo
        speed.y = (y + 200) / 15

def inside(xy):
    "Retorna True si la coordenada está dentro de la pantalla."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Dibujar la bola y los balones (objetivos)."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')  # Dibujar los balones

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')  # Dibujar la bola

    update()

def move():
    "Mover la bola y los balones."
    if randrange(30) == 0: 
        y = randrange(-150, 150)
        target = vector(200, y)  
        targets.append(target)

    for target in targets:
        target.x -= 2  # Aumentar la velocidad de los balones (más rápido)

    if inside(ball):
        speed.y -= 0.35  
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Reposicionar balones que salen de la pantalla
    for target in targets:
        if not inside(target):
            target.x = 200  # Reposicionar el balón a la derecha si sale de la pantalla

    ontimer(move, 30)  # Actualizar más rápido el movimiento


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)  
move()
done()
