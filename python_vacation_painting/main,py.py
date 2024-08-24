# import turtle
#
# tim = turtle.Turtle()
# screen = turtle.Screen()

import turtle as t

tim = t.Turtle()
s = t.Screen()

s.setup(width=650, height=800)       # .setup() -> screen의 사이즈를 설정
s.bgcolor("lightcyan")               # .bgcolor() -> screen의 배경색깔

tim.pensize(5)                       # .pensize() -> 펜사이즈 지정
tim.speed(1)
tim.color("black", "#f0a53a")

# body
tim.penup()                         # .penup() -> 그리지 않고 위치만 이동
tim.goto(x=-90, y=20)               # .goto() -> 특정 위치로 이동
tim.pendown()
tim.begin_fill()                    # .begin_fill() -> 이제부터 그리는 영역은 채우기 시작
tim.setheading(220)
tim.circle(80, 100)     # 반지름이 80인 원의 100도 만큼 그리는 메서드
tim.setheading(270)
tim.forward(100)
tim.circle(35, 180)
tim.forward(20)
tim.right(90)
tim.forward(40)
tim.right(90)
tim.forward(20)
tim.circle(35, 180)
tim.forward(100)
tim.setheading(40)
tim.circle(80, 100)
tim.goto(-90, 20)
tim.end_fill()

#arms, body
# left arm
tim.penup()
tim.goto(-90, -30)
tim.pendown()
tim.goto(-90, -100)
# right arm
tim.penup()
tim.goto(90, -30)
tim.pendown()
tim.goto(90, -100)

# white decoration on chest
tim.color("white", "white")
tim.penup()
tim.goto(40, -40)
tim.pendown()
tim.begin_fill()
tim.goto(20, -60)
tim.goto(0,-40)
tim.goto(-20, -60)
tim.goto(-40, -40)
tim.setheading(240)
tim.circle(47, 240)
tim.end_fill()

#ears
tim.color("black", "#f0a53a")
#left ear
tim.penup()
tim.goto(-70, 210)
tim.pendown()
tim.begin_fill()
tim.setheading(120)
tim.circle(30, 210)
tim.end_fill()

#right ear
tim.penup()
tim.goto(70, 210)
tim.pendown()
tim.begin_fill()
tim.setheading(60)
tim.circle(-30, 210)                    # radius를 음수로 잡으면 시계방향 회전
tim.end_fill()

#face
tim.penup()
tim.goto(0, 230)
tim.pendown()
tim.begin_fill()
tim.setheading(180)
tim.circle(130)
tim.end_fill()

#eyes nose ...
#left eyebrow
tim.pensize(10)                             # 펜의 두께
tim.penup()
tim.goto(-80, 130)
tim.pendown()
tim.goto(-30, 130)
#right eyebrow
tim.penup()
tim.goto(80, 130)
tim.pendown()
tim.goto(30, 130)

#left eye
tim.penup()
tim.goto(-55, 110)
tim.pendown()
tim.dot(15)                 # .dot() 현재 좌표를 중심으로 점을 찍음.
#right eye
tim.penup()
tim.goto(55, 110)
tim.pendown()
tim.dot(15)

#nose
tim.pensize(5)
tim.color("black", "white")
tim.penup()
tim.goto(-10, 80)
tim.pendown()
tim.begin_fill()
tim.setheading(155)
tim.circle(18, 240)
tim.circle(25, 25)
tim.right(116)
tim.circle(25, 25)
tim.circle(18, 240)
tim.goto(0, 80)
tim.dot(20)
tim.end_fill()

tim.hideturtle()            # 거북이(화살표) 모양이 보이지 않게 숨기기













s.exitonclick()