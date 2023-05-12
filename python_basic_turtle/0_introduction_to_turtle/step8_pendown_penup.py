from turtle import *

pendown()  # ペンをさげる
shape('turtle')  # turtle, circle, arrow, classic
forward(100)
penup()  # ペンをあげる
right(90)
forward(100)
left(90)
pendown()  # ペンをさげる
forward(200)
backward(50)
penup()  # ペンをあげる
goto(0, 0)

mainloop()