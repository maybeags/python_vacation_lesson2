from turtle import Turtle, Screen
import random

tim = Turtle()      # 객체 생성
screen = Screen()
tim.shape("turtle")
tim.color("white")
screen.bgcolor("black")
colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
]
# for _ in range(4):
#     for _ in range(10):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#     tim.left(90)

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(75)
        tim.left(angle)





# .heading()

# heading()은 거북이가 바라보는 방향을 나타내는 속성이고, 도(degree)단위로 표현됨. 시계 방향으로 측정
# 0도 : 오른쪽
# 90도 : 위쪽
# 180도 : 왼쪽
# 270도 : 아래쪽
# .setheading()
# 특정 각도로 거북이를 회전시키는 메서드

print(tim.heading())

tim.setheading(30)

# for n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(n)


def draw_spriograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        tim.color(random.choice(colours))
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

tim.speed(0)
draw_spriograph(1)






screen.exitonclick()