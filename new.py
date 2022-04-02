from turtle import *
import colorsys

bgcolor('black')
pensize(2)
hue = 0.0
speed(500)


for i in range(500):
    col = colorsys.hsv_to_rgb(hue,1,1)
    pencolor(col)
    hue += 0.005

    rt(i)
    circle(100, i)
    fd(i)
    rt(90)

done()