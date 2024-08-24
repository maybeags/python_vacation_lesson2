from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("white")

screen = Screen()
screen.bgcolor("black")

for _ in range(3):
    tim.forward(100)
    tim.left(120)

for _ in range(4):
    tim.forward(100)
    tim.left(90)

# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# tim.left(90)
#
# for _ in range(10):
#     tim.forward(10)
#     tim.color("black")
#     tim.forward(10)
#     tim.color("white")


screen.exitonclick()