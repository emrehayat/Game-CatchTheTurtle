import turtle
import math
import random

score = 0
print ("\n" * 3)
print("Your score is: 0")

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Beni Yakala :)")

my_writing = turtle.Pen()
my_writing.pencolor("purple")
my_writing.hideturtle()
my_writing.penup()
my_writing.setposition(-250,330)
my_writing.write("CATCH THE PURPLE TURTLE", font=("Verdana", 25))

text=turtle.Pen()
text.pencolor("red")
text.hideturtle()
text.penup()
text.setposition(-180, 300)
text.write("DON'T TOUCH THE EDGES!", font=("Verdana", 18))

my_turtle = turtle.Turtle()
my_turtle.color("orange")
my_turtle.shape("turtle")
my_turtle.penup()
my_turtle.speed(0)
my_turtle.shapesize(1.5)

goal = turtle.Turtle()
goal.color("purple")
goal.shape("turtle")
goal.penup()
goal.speed(0)
goal.setposition(-125, 200)

speed = 2

my_pen = turtle.Turtle()
my_pen.penup()
my_pen.speed(10)
my_pen.hideturtle()
my_pen.setposition(-275,-275)
my_pen.pendown()
for i in range(4):
    my_pen.color("yellow")
    my_pen.forward(275/2)
    my_pen.color("red")
    my_pen.forward(275/2)
    my_pen.color("blue")
    my_pen.forward(275/2)
    my_pen.color("purple")
    my_pen.forward(275/2)
    my_pen.left(90)
my_pen.hideturtle()

def jump():
    my_turtle.forward(100)

def turn_back():
    my_turtle.left(180)
def turn_left():
    my_turtle.left(30)
def turn_right():
    my_turtle.right(30)

drawing_board.listen()
drawing_board.onkey(jump, "Up")
drawing_board.onkey(turn_back, "Down")
drawing_board.onkey(turn_left, "Left")
drawing_board.onkey(turn_right, "Right")

while True:
    my_turtle.forward(speed)

    if my_turtle.xcor() > 275 or my_turtle.xcor() < -275:
        print("GAME OVER")
        quit()

    if my_turtle.ycor() > 275 or my_turtle.ycor() < -275:
        print("GAME OVER")
        quit()

    d = math.sqrt(math.pow(my_turtle.xcor() - goal.xcor(), 2) + math.pow(my_turtle.ycor() - goal.ycor(), 2))
    if d < 15:
        goal.setposition(random.randint(-275, 275), random.randint(-275, 275))
        score += 1
        print("\n" * 3)
        print(f"Your score is: {score}")

turtle.done()