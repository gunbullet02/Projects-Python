import turtle

tut = turtle.Screen()

tut.bgcolor("green")

tut.title("Turtle")
my_pen = turtle.Turtle()

my_pen.color("orange")
tut = turtle.Screen()

for i in range(4):
    my_pen.forward(100)
    my_pen.left(90)

my_pen.goto(50,50)

for i in range(4):
    my_pen.forward(100)
    my_pen.left(90)

my_pen.goto(100,100)
my_pen.goto(150,150)

my_pen.goto(50,150)
my_pen.goto(0,100)

