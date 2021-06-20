import turtle
import datetime as dt
import time

# turtule obect to display time
t = turtle.Turtle()

r_box = turtle.Turtle()
s = turtle.Screen()
s.title('Digital Clock by @abhinavakp')
s.bgcolor('Green')

# obtain current time from system
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour
r_box.pensize(3)
r_box.color('black')
r_box.penup()
r_box.goto(-20, 0)
r_box.pendown()

for intex in range(2):
    r_box.forward(230)
    r_box.left(90)
    r_box.forward(60)
    r_box.left(90)

r_box.hideturtle()

while True:
    t.hideturtle()
    t.clear()

    t.write(str(hr).zfill(2) + ":" +
            str(min).zfill(2) + ":" +
            str(sec).zfill(2), font=("Arial Narrow", 35, "bold") )
    time.sleep(1)
    sec += 1

    if sec == 60:
        sec = 0
        min += 1

    if min == 60:
        min = 0
        hr += 1

    if hr == 13:
        hr = 1