import turtle
import numpy as np
from random import randint

def main(speed=0, bg_color="grey"):
    # create Turtle object
    turtle_screen = turtle.Screen()
    myTurtle = turtle.Turtle()

    turtle.colormode(255)
    # set speed to 'fastest = 0'
    myTurtle.speed(speed) #change speed
    # change background color
    turtle_screen.bgcolor(bg_color)
  
 
    """TODO: define different colors here"""

    #c= ['red','green','blue','yellow','black','grey','white','pink','orange','purple']

    for i in range(10):
        # define some params
        size = 18
        pos = [np.random.randint(-300, 300), np.random.randint(-300, 300)]

        """TODO: set snowflake color here (one of the colors defined above)"""

        # Go to the start position of the snowflake
        myTurtle.penup()
        myTurtle.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
        myTurtle.goto(pos[0], pos[1])
        myTurtle.pendown()

        # draw the snowflake
        for _ in range(8):
            snowflake_branch(size, myTurtle)
            myTurtle.left(45)

    turtle_screen.mainloop()

def snowflake_branch(size, myTurtle):
    # This function draws one branch of the snowflake.
    for _ in range(3):
        for _ in range(3):
            myTurtle.forward(size / 3)
            myTurtle.backward(size / 3)
            myTurtle.right(45)
        myTurtle.left(90)
        myTurtle.backward(size / 3)
        myTurtle.left(45)
    myTurtle.right(90)
    myTurtle.forward(size)


if __name__ == "__main__":
    main()
