# imported turtle module
import turtle

wind = turtle.Screen()
wind.title("ping pong by SERAG")
wind.bgcolor("white")
wind.setup(width=800, height=600)
wind.tracer(0)
#xxxx
play1 = turtle.Turtle()
play1.speed(0)
play1.shape("square")
play1.color("blue")
play1.shapesize(stretch_wid=5, stretch_len=1)
play1.penup()
play1.goto(-350, 0)
#madreb 2
play2 = turtle.Turtle()
play2.speed(0)
play2.shape("square")
play2.color("red")
play2.shapesize(stretch_wid=5, stretch_len=1)
play2.penup()
play2.goto(350, 0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = .350
ball.dy = .350

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player1 : 0  player 2 : 0 ", align="center", font=("Courier",24,"normal"))


#functions
def play1_up():
    y = play1.ycor()
    y += 20
    play1.sety(y)
def play1_down():
        y = play1.ycor()
        y -= 20
        play1.sety(y)

def play2_up():
     y = play2.ycor()
     y += 20
     play2.sety(y)

def play2_down():
     y = play2.ycor()
     y -= 20
     play2.sety(y)

#keyboard bindings
wind.listen()
wind.onkeypress(play1_up, "w")

wind.onkeypress(play1_down, "s")

wind.onkeypress(play2_up, "Up")

wind.onkeypress(play2_down, "Down")

while True:
    wind.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player1: {} player 2: {} ".format(score1, score2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player1: {} player 2: {} ".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    #when the ball heat the play
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < play2.ycor() + 40 and ball.ycor() > play2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < play1.ycor() + 40 and ball.ycor() > play1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

