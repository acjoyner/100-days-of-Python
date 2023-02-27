import random
import turtle as t

tim = t.Turtle()

colors = ["dark magenta","orange red","green"]
directions = [0, 90, 188, 270]
#screen = Screen()

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))


#screen.exitonclick()