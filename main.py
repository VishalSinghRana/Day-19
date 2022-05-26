from turtle import Turtle, Screen
import random
#tim = Turtle()

screen = Screen()

# def move_forwards():  # user defined function that moves the turtle or cursor 10 spaces forward.
#     tim.forward(10)


# screen.listen()  # in order to listen to the keyboard commands we need to use this listen() function.

# onkey(function,key) :- is a function that accepts 2 argument. function is what the particular key will do
# (user defined function) and key is the key name like space, up, down etc.

# screen.onkey(key='space', fun=move_forwards)  # this will move the turtle 10steps forward everytime we hit 'space' key.
#
# screen.exitonclick()

# MAKING AN ETCH A SKETCH APP (free drawing on the screen.)

# screen.listen()
# tom = Turtle()
#
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def right_turn():
#     tim.right(30)
#
#
# def left_turn():
#     tim.left(30)
#
#
# def clear():
#     tim.clear()
#     tim.setheading(0)
#     tim.penup()
#     tim.setpos(0, 0)
#     tim.pendown()
#     tim.speed(0)


# screen.onkey(key='w', fun= move_forward)
# screen.onkey(key='d', fun=right_turn)
# screen.onkey(key='s', fun=move_backward)
# screen.onkey(key='a', fun=left_turn)
# screen.onkey(key='c', fun=clear)
#
# screen.exitonclick()

# OBJECT STATE & INSTANCE

# UNDERSTANDING THE TURTLE COORDINATE SYSTEM.
is_race_on = False
screen.setup(width=500, height=400)  # height and width of the display screen.

user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race(vibgyor color)')
# textinput() method pops up a window screen and ask for user input.

# we already have a screen of 500*400 and if we want our turtle to go to the extreme left we will use the goto function.

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
turtles = []

for i in range(7):
    turtle = colors[i]
    turtle = Turtle(shape='turtle')
    turtle.color(colors[i])
    turtles.append(turtle)

y_axis = -140

for turtle in turtles:
    turtle.penup()
    turtle.goto(x=-240, y=y_axis+30)
    y_axis = y_axis + 30

if user_bet :
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won.Turtle {winning_turtle} won the race.")
            else:
                print(f"You lose. Turtle {winning_turtle} won the race.")

        step = random.randint(0, 10)
        turtle.forward(step)

# tim = Turtle(shape='turtle')
# tim.penup()
# tim.goto(x=-240, y=0)
screen.exitonclick()


































