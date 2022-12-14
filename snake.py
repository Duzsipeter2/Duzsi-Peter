import turtle
import random

w = 500
h = 500
kaja_meret = 10
delay = 100

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def reset():
    global snake, snake_ir, kaja_hely, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_ir = "up"
    kaja_hely = get_random_kaja_hely()
    kaja.goto(kaja_hely)
    move_snake()


def move_snake():
    global snake_ir

    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_ir][0]
    new_head[1] = snake[-1][1] + offsets[snake_ir][1]

    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)

        if not food_collision():
            snake.pop(0)

        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h

        pen.clearstamps()

        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()

        turtle.ontimer(move_snake, delay)


def food_collision():
    global kaja_hely
    if get_distance(snake[-1], kaja_hely) < 20:
        kaja_hely = get_random_kaja_hely()
        kaja.goto(kaja_hely)
        return True
    return False


def get_random_kaja_hely():
    x = random.randint(- w / 2 + kaja_meret, w / 2 - kaja_meret)
    y = random.randint(- h / 2 + kaja_meret, h / 2 - kaja_meret)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance


def go_up():
    global snake_ir
    if snake_ir != "down":
        snake_ir = "up"


def go_right():
    global snake_ir
    if snake_ir != "left":
        snake_ir = "right"


def go_down():
    global snake_ir
    if snake_ir != "up":
        snake_ir = "down"


def go_left():
    global snake_ir
    if snake_ir != "right":
        snake_ir = "left"


screen = turtle.Screen()
screen.setup(w, h)
screen.title("Kigy??s")
screen.bgcolor("green")
screen.setup(500, 500)
screen.tracer(0)

pen = turtle.Turtle("square")
pen.penup()

kaja = turtle.Turtle()
kaja.shape("square")
kaja.color("red")
kaja.shapesize(kaja_meret / 20)
kaja.penup()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

reset()
turtle.done()