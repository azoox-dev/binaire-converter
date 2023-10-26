from turtle import *

def carre(size, content_color, pen_color, nb_write):
    speed(0)
    color(pen_color)
    begin_fill()
    fillcolor(content_color)
    for _ in range(4):
        fd(size)
        rt(90)
    end_fill()
    middle_x = xcor() - size / 2
    middle_y = ycor() - size / 2
    up()
    goto(middle_x, middle_y)
    fd(size)
    write(str(nb_write), align="center", font=("Arial", 12, "normal"))
    down()
