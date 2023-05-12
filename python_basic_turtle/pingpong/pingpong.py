import turtle

# ウィンドウの表示
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)
sc.tracer(0)

# ボールの表示
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(400, 0)

# 左側のバー表示
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=0.1)
left_pad.penup()
left_pad.goto(-400, 0)

# 右側のバー表示
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=0.1)
right_pad.penup()
right_pad.goto(400, 0)

dx = 3
dy = 3

# 点数初期値
left_score = 0
right_score = 0

# 点数表示
sketch = turtle.Turtle()
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write(
    "0 vs 0",
    align="center",
    font=("Courier", 24, "normal")
)

# 左側のバーの動き
def up_left_paddle():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def down_left_paddle():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)


# 右側のバーの動き
def up_right_paddle():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)


def down_right_paddle():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


# キーボード操作の情報
sc.listen()
sc.onkeypress(up_left_paddle, "w")
sc.onkeypress(down_left_paddle, "s")
sc.onkeypress(up_right_paddle, "Up")
sc.onkeypress(down_right_paddle, "Down")


while True:
    sc.update()

    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    # 加点条件
    if ball.ycor() > 280:
        dy *= -1

    if ball.ycor() < -280:
        dy *= -1

    if ball.xcor() > 500:
        ball.goto(0, 0)
        left_score += 1
        sketch.clear()
        sketch.write(
            "{} vs {}".format(left_score, right_score),
            align="center",
            font=("Courier", 24, "normal")
        )

    if ball.xcor() < -500:
        ball.goto(0, 0)
        right_score += 1
        sketch.clear()
        sketch.write(
            "{} vs {}".format(left_score, right_score),
            align="center",
            font=("Courier", 24, "normal")
        )

    if (ball.distance(left_pad)  < 40 and ball.xcor() < -400) or (
        ball.distance(right_pad) < 40 and ball.xcor() >  400):
        dx *= -1