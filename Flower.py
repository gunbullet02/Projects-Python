import turtle

sc = turtle.Screen()

pen = turtle.Turtle()

col = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

sc.setup(500, 500)

sc.bgcolor('black')

pen.pensize(4)

pen.speed(20)

i = 0

for angle in range(0, 360, 12):

    pen.color(col[i])

    if i == 6:
        i = 0

    else:
        i += 1

    pen.seth(angle)

    pen.circle(80)

pen.ht()