import turtle as t
import colorsys as cs
t.bgcolor('black')
t.speed(20)

color = ['steelblue', 'coral', 'magenta', 'palegreen']
for i in range(300):
    t.pencolor(color[i % 4])
    t.rt(i)
    t.circle(120, i)
    t.fd(i)
    t.rt(90)
t.done()