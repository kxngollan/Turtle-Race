import turtle
import random

screen = turtle.Screen()
screen.screensize(500, 500)

colors = ["red", "green", "blue", "yellow", "black", "orange", "pink"]
random.shuffle(colors)
y_positions = [-200, -140, -80, -20, 40, 100, 160, 220]
turtles = []

taking_bets = True

while taking_bets:
    user_bet = screen.textinput(title="Turtle Race", prompt="Which turtle will win the race? Enter a color:\n "
                                                            "Red/Green/Blue/Yellow/Black/"
                                                            "\nOrange/Pink").lower()
    if user_bet in colors:
        taking_bets = False

for i in range(len(colors)):
    myturtle = turtle.Turtle(shape="turtle")
    myturtle.color(colors[i])
    myturtle.penup()
    myturtle.goto(x=-230, y=y_positions[i])
    turtles.append(myturtle)

if user_bet:
    racing = True

while racing:
    for myturtle in turtles:
        if myturtle.xcor() > 230:
            racing = False
            winning_color = myturtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        myturtle.forward(rand_distance)

screen.exitonclick()
