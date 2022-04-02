import turtle

colors = ['yellow', 'green', 'red', 'white', 'cyan', 'blue']

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('Black')
t.speed(10.5)
t.hideturtle()

for i in range(100):
    t.circle(50)
    t.color(colors[i%6])
    t.fd(i*5)
    t.left(500)
    t.width(2)