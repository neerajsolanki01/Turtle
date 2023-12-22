import turtle
import colorsys

t=turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')
h=0

for i in range(360):
    c=colorsys.hsv_to_rgb(h, 1, 0.8)
    t.color(c)
    t.goto(0, 0)
    t.fd(100+i/5)

    t.right(100)
    t.fd(100+i/4)
    t.lt(70)
    t.right(71)
    h = h+0.104

