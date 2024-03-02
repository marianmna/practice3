from turtle import *
import turtle

t = turtle.Turtle()
w = turtle.Screen()

t.begin_fill()
t.fillcolor('blue')
t.circle(100, 45)
t.end_fill()

t.begin_fill()
t.fillcolor('brown')
t.circle(100, 65)
t.end_fill()

t.begin_fill()
t.fillcolor('green')
t.circle(100, 90)
t.end_fill()

t.begin_fill()
t.fillcolor('orange')
t.circle(100, 45)
t.end_fill()

t.begin_fill()
t.fillcolor('yellow')
t.circle(100, 35)
t.end_fill()

t.begin_fill()
t.fillcolor('red')
t.circle(100, 80)
t.end_fill()

w.mainloop()