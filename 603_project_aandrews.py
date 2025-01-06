#
# SEIS 603-03 Project
# Authors: Ashton Andrews, Anton Andrews
import turtle as t


# import random


def oneside():
    wn = t.Screen()
    timmy = t.Turtle()
    timmy.pensize(1)
    timmy.speed(0)
    timmy.color("blue")
    count1 = 0
    # timmy.stamp()

    # Place marker to the top left
    timmy.up()
    timmy.lt(90)
    timmy.fd(375)
    timmy.lt(90)
    timmy.fd(750)
    timmy.rt(180)
    timmy.down()
    # Place marker to the top left

    for count in range(8):

        for count in range(25):
            timmy.down()
            timmy.rt(60)
            timmy.fd(100)

            timmy.down()
            timmy.lt(180)
            timmy.fd(100)

            timmy.up()
            timmy.rt(120)
            timmy.fd(100)
        count1 += 100
        timmy.up()
        #timmy.rt(90)
        # timmy.rt(90)
        # timmy.fd(100)
        # timmy.rt(90)
        # timmy.fd(1000)
        # timmy.lt(180)
        timmy.goto(-750,375)
        timmy.right(90)
        timmy.fd(count1)
        timmy.lt(90)
        timmy.down()
        #count1 += 100
    # timmy.right(1)

    wn.exitonclick()


def twosides():

    wn = t.Screen()
    timmy = t.Turtle()
    t.pensize(3)
    t.speed()
    t.fillcolor("green")
    count = 0

    for x in range(4):
        t.begin_fill()
        timmy.setheading(count + 25)
        t.circle(-135, 90)
        t.right(90)
        t.circle(-135, 90)
        t.end_fill()


    # timmy.left(180)
    # timmy.fd(7)
    # timmy.bk(7)
    # timmy.right(180)
    #
    # timmy.left(90)
    # for x in range(180):
    #     timmy.forward(2)
    #     timmy.right(1)
    # timmy.left(90)
    # timmy.fd(7)
    # timmy.bk(7)
    # timmy.right(90)
    # for y in range(180):
    #     timmy.forward(2)
    #     timmy.right(1)


    wn.exitonclick()

def threesides():

    wn = t.Screen()
    timmy = t.Turtle()
    timmy.pensize(3)
    timmy.speed(0)
    # timmy.stamp()

    for count in range(120):
        timmy.down()
        timmy.fd(200)
        timmy.left(120)

        timmy.fd(200)
        timmy.left(120)

        timmy.fd(200)
        timmy.left(120)

        timmy.right(3)

    wn.exitonclick()

def foursides():
    num = int(input("Enter 1 (for a grid art) or 2 (for abstract art): "))

    if num == 1:
        wn = t.Screen()
        timmy = t.Turtle()
        timmy.pensize(3)
        timmy.speed(6)

        timmy.up()
        timmy.back(100)
        timmy.down()

        for a in range(4):
            # Draws 4 rows of squares

            timmy.down()
            timmy.forward(50)
            timmy.left(90)
            timmy.forward(50)
            timmy.left(90)
            timmy.forward(50)
            timmy.left(90)
            timmy.forward(50)
            timmy.left(90)

            for iter in range(3):
                timmy.forward(100)
                timmy.left(90)
                timmy.forward(50)
                timmy.left(90)
                timmy.forward(50)
                timmy.left(90)
                timmy.forward(50)
                timmy.left(90)

            timmy.up()
            timmy.back(150)
            timmy.right(90)
            timmy.forward(50)
            timmy.left(90)

            # # Draw the inner square
            # for count in range(4):
            #     timmy.forward(100)
            #     timmy.left(90)
            #
            # timmy.right(110)

        wn.exitonclick()

    elif num == 2:
        wn = t.Screen()
        timmy = t.Turtle()
        timmy.pensize(3)
        timmy.speed(0)

        for iter in range(40):
            for count in range(4):  # Draw the outer square
                timmy.forward(200)
                timmy.left(90)
            timmy.stamp()

            # Moves turtle's position to start the inner square
            timmy.up()
            timmy.forward(50)
            timmy.left(90)
            timmy.forward(50)
            timmy.down()
            timmy.right(90)

            # Draw the inner square
            for count in range(4):
                timmy.forward(100)
                timmy.left(90)

            timmy.right(110)

        wn.exitonclick()
    else:
        print("Please enter 1 or 2 next time!")

def fivesides():

    wn = t.Screen()
    timmy = t.Turtle()
    timmy.pensize(3)
    timmy.speed(0)
    # timmy.stamp()

    # Place marker to the top left
    timmy.up()
    timmy.lt(90)
    timmy.fd(250)
    timmy.lt(90)
    timmy.fd(650)
    timmy.rt(180)
    timmy.down()
    # Place marker to the top left

    the_x = -500
    the_y = 300

    # Top row of boomerang being thrown
    for count in range(15):
        timmy.down()
        timmy.rt(30)
        timmy.fd(100)

        timmy.lt(165)
        timmy.fd(110)

        timmy.lt(45)
        timmy.fd(20)

        timmy.lt(45)
        timmy.fd(100)

        timmy.lt(162)
        timmy.fd(95)

        timmy.up()
        timmy.goto(the_x, the_y)
        the_x += 200
        the_y -= 20

    the_x2 = 750
    the_y2 = -200

    # Bottom row of boomerang being thrown
    for count in range(15):
        timmy.goto(the_x2, the_y2)
        timmy.down()
        timmy.rt(30)
        timmy.fd(100)

        timmy.lt(165)
        timmy.fd(110)

        timmy.lt(45)
        timmy.fd(20)

        timmy.lt(45)
        timmy.fd(100)

        timmy.lt(162)
        timmy.fd(95)

        timmy.up()
        timmy.goto(the_x, the_y)
        the_x2 -= 200
        the_y2 -= 20

    wn.exitonclick()


def sixsides():

    wn = t.Screen()
    timmy = t.Turtle()
    timmy.pensize(3)
    timmy.speed(0)
    timmy.up()
    timmy.right(90)
    timmy.forward(200)
    timmy.left(90)
    # timmy.stamp()
    #mult = 1
    vari = 60
    timmy.fillcolor("gold")
    for x in range(1):
        # randx = random.randrange(0, 80, 30)
        # randy = random.randrange(0, 60, 30)
        for count in range(6):
            timmy.begin_fill()
            for a in range(6):

                timmy.down()
                timmy.forward(vari)  # fd(30)
                timmy.left(60)
            timmy.up()
            timmy.forward(vari)
            timmy.left(60)
            timmy.forward(vari)
            timmy.right(60)
            timmy.forward(vari)
            timmy.left(60)
            timmy.end_fill()
        #mult+=1

        timmy.goto(181, 8)

        for count in range(6):
            timmy.begin_fill()
            for a in range(6):
                timmy.down()
                timmy.forward(vari)  # fd(30)
                timmy.left(60)
            timmy.up()
            timmy.forward(vari)
            timmy.left(60)
            timmy.forward(vari)
            timmy.right(60)
            timmy.forward(vari)
            timmy.left(60)
            timmy.end_fill()
            # timmy.up()
            # timmy.forward(30)
            # timmy.right(60)
            # timmy.forward(30)
            # timmy.right(60)
            # timmy.forward(30)
            # timmy.left(60)

        timmy.goto(-181, 8)

        for count in range(6):
            timmy.begin_fill()
            for a in range(6):
                timmy.down()
                timmy.forward(vari)  # fd(30)
                timmy.left(60)
            timmy.up()
            timmy.forward(vari)
            timmy.left(60)
            timmy.forward(vari)
            timmy.right(60)
            timmy.forward(vari)
            timmy.left(60)
            timmy.end_fill()
            # timmy.up()
            # timmy.forward(30)
            # timmy.left(60)
            # timmy.forward(30)
            # timmy.right(60)
            # timmy.forward(30)
            # timmy.right(60)

        timmy.goto(181, -408)

        for count in range(6):
            timmy.begin_fill()
            for a in range(6):
                timmy.down()
                timmy.forward(vari)  # fd(30)
                timmy.left(60)
            timmy.up()
            timmy.forward(vari)
            timmy.left(60)
            timmy.forward(vari)
            timmy.right(60)
            timmy.forward(vari)
            timmy.left(60)
            timmy.end_fill()
            # timmy.up()
            # timmy.forward(30)
            # timmy.right(60)
            # timmy.forward(30)
            # timmy.right(60)
            # timmy.forward(30)
            # timmy.left(60)
            # timmy.forward(30)
            # timmy.left(60)

        timmy.goto(-181, -408)

        for count in range(6):
            timmy.begin_fill()
            for a in range(6):
                timmy.down()
                timmy.forward(vari)  # fd(30)
                timmy.left(60)
            timmy.up()
            timmy.forward(vari)
            timmy.left(60)
            timmy.forward(vari)
            timmy.right(60)
            timmy.forward(vari)
            timmy.left(60)
            timmy.end_fill()
            # timmy.up()
            # timmy.forward(30)
            # timmy.left(60)
            # timmy.forward(30)
            # timmy.left(60)
            # timmy.forward(30)
            # timmy.right(60)
            # timmy.forward(30)
            # timmy.left(60)
        #timmy.goto(randx, randy)


        timmy.goto(-360, -200)

        for count in range(6):
            timmy.begin_fill()
            for a in range(6):
                timmy.down()
                timmy.forward(vari)  # fd(30)
                timmy.left(60)
            timmy.up()
            timmy.forward(vari)
            timmy.left(60)
            timmy.forward(vari)
            timmy.right(60)
            timmy.forward(vari)
            timmy.left(60)
            timmy.end_fill()


        timmy.goto(360, -200)

        for count in range(6):
            timmy.begin_fill()
            for a in range(6):
                timmy.down()
                timmy.forward(vari)  # fd(30)
                timmy.left(60)
            timmy.up()
            timmy.forward(vari)
            timmy.left(60)
            timmy.forward(vari)
            timmy.right(60)
            timmy.forward(vari)
            timmy.left(60)
            timmy.end_fill()


        timmy.goto(0, 215)

        for count in range(6):
            timmy.begin_fill()
            for a in range(6):
                timmy.down()
                timmy.forward(vari)  # fd(30)
                timmy.left(60)
            timmy.up()
            timmy.forward(vari)
            timmy.left(60)
            timmy.forward(vari)
            timmy.right(60)
            timmy.forward(vari)
            timmy.left(60)
            timmy.end_fill()


        timmy.goto(0, -615)

        for count in range(6):
            timmy.begin_fill()
            for a in range(6):
                timmy.down()
                timmy.forward(vari)  # fd(30)
                timmy.left(60)
            timmy.up()
            timmy.forward(vari)
            timmy.left(60)
            timmy.forward(vari)
            timmy.right(60)
            timmy.forward(vari)
            timmy.left(60)
            timmy.end_fill()

    wn.exitonclick()

def sevensides():

    wn = t.Screen()
    timmy = t.Turtle()
    timmy.pensize(3)
    timmy.speed(0)
    timmy.fillcolor("silver")
    # timmy.stamp()

    timmy.up()
    timmy.right(90)
    timmy.forward(150)
    timmy.left(90)
    timmy.back(72)

    timmy.begin_fill()
    for count in range(7):
        timmy.down()
        timmy.forward(140)
        timmy.left(360/7)
    timmy.end_fill()

    graphic_size = 90
    timmy.fillcolor("snow3")
    timmy.penup()
    timmy.goto(0, (-3/32)*graphic_size)
    timmy.left(180)
    timmy.down()
    timmy.begin_fill()
    for i in range(2):
        timmy.circle(-graphic_size/2,270)
        timmy.right(90)
        timmy.forward((3/16) *graphic_size)
        timmy.right(90)
        timmy.circle((5/16) * graphic_size, 270)
    timmy.end_fill()
    timmy.up()
    timmy.goto((-3/16) * graphic_size, graphic_size)
    timmy.right(180)
    timmy.down()
    for i in range(2):
        timmy.begin_fill()
        for x in range(2):
            timmy.forward((2/16)*graphic_size)
            timmy.right(90)
            timmy.forward(2*graphic_size)
            timmy.right(90)
        timmy.end_fill()
        timmy.up()
        timmy.goto((1/16)*graphic_size, graphic_size)
        timmy.down()

    # timmy.up()
    # timmy.goto(0,0)
    # timmy.goto(125,5)
    # timmy.down()
    # timmy.left(90)
    # timmy.pensize(2)
    # for x in range(270):
    #     timmy.forward(0.5)
    #     timmy.right(0.25)
    # for y in range(270):
    #     timmy.forward(0.5)
    #     timmy.left(0.25)

    wn.exitonclick()


def eightsides():

    wn = t.Screen()
    timmy = t.Turtle()
    timmy.pensize(7)
    timmy.speed(0)
    # timmy.stamp()

    timmy.up()
    timmy.lt(90)
    timmy.fd(250)
    timmy.lt(90)
    timmy.fd(100)
    timmy.rt(180)
    timmy.down()
    timmy.color("chocolate")

    timmy.begin_fill()
    for i in range(8):

        timmy.fd(200)
        timmy.rt(45)
    timmy.end_fill()

    timmy.up()
    timmy.lt(90)
    timmy.fd(25)
    timmy.lt(90)
    timmy.fd(10)
    timmy.rt(180)
    timmy.down()
    timmy.color("brown")

    for i in range(8):

        timmy.fd(225)
        timmy.rt(45)
    #Add numbers to the clock

    timmy.color("black")
    #12
    timmy.up()
    timmy.fd(80)
    timmy.rt(90)
    timmy.fd(100)
    timmy.down()
    timmy.write("12", font=("Arial", 50, "normal"))

    # 1
    timmy.up()
    timmy.fd(10)
    timmy.lt(90)
    timmy.fd(120)
    timmy.down()
    timmy.write("1", font=("Arial", 50, "normal"))

    # 2
    timmy.up()
    timmy.fd(70)
    timmy.rt(90)
    timmy.fd(70)
    timmy.down()
    timmy.write("2", font=("Arial", 50, "normal"))

    # 3
    timmy.up()
    timmy.fd(130)
    timmy.lt(90)
    timmy.fd(40)
    timmy.down()
    timmy.write("3", font=("Arial", 50, "normal"))

    # 4
    timmy.up()
    timmy.rt(90)
    timmy.fd(115)
    timmy.rt(90)
    timmy.fd(40)
    timmy.down()
    timmy.write("4", font=("Arial", 50, "normal"))

    # 5
    timmy.up()
    timmy.fd(75)
    timmy.lt(90)
    timmy.fd(75)
    timmy.down()
    timmy.write("5", font=("Arial", 50, "normal"))

    # 6
    timmy.up()
    timmy.rt(90)
    timmy.fd(95)
    timmy.lt(90)
    timmy.fd(15)
    timmy.down()
    timmy.write("6", font=("Arial", 50, "normal"))

    # 7
    timmy.up()
    timmy.rt(90)
    timmy.fd(100)
    timmy.lt(90)
    timmy.bk(12)
    timmy.down()
    timmy.write("7", font=("Arial", 50, "normal"))

    # 8
    timmy.up()
    timmy.rt(90)
    timmy.fd(80)
    timmy.lt(90)
    timmy.bk(70)
    timmy.down()
    timmy.write("8", font=("Arial", 50, "normal"))

    # 9
    timmy.up()
    timmy.rt(90)
    timmy.fd(42)
    timmy.lt(90)
    timmy.bk(120)
    timmy.down()
    timmy.write("9", font=("Arial", 50, "normal"))

    # 10
    timmy.up()
    timmy.rt(90)
    timmy.bk(15)
    timmy.lt(90)
    timmy.bk(120)
    timmy.down()
    timmy.write("10", font=("Arial", 50, "normal"))

    # 11
    timmy.up()
    timmy.rt(90)
    timmy.bk(80)
    timmy.lt(90)
    timmy.bk(80)
    timmy.down()
    timmy.write("11", font=("Arial", 50, "normal"))

    #.
    timmy.up()
    timmy.goto(-15,-40)
    timmy.write(".", font=("Arial", 100, "bold"))

    timmy.pensize(2)
    timmy.down()
    timmy.stamp()
    timmy.home()

    timmy.fd(125)
    timmy.stamp()

    timmy.hideturtle()

    wn.exitonclick()


def main():

    print("Choose a number of from 1-8, these will represent the number of sides. Enter 0 to exit.\n"
                        "This Program will create shapes/objects with the number of sides that you choose!")
    while True:
        num = input("Enter the number of sides you would like: ")

        if num == "1":
            oneside()
            print("Thank you for trying our Shape Maker Program! Exiting the program...")
            break
        elif num == "2":
            twosides()
            print("Thank you for trying our Shape Maker Program! Exiting the program...")
            break
        elif num == "3":
            threesides()
            print("Thank you for trying our Shape Maker Program! Exiting the program...")
            break
        elif num == "4":
            foursides()
            print("Thank you for trying our Shape Maker Program! Exiting the program...")
            break
        elif num == "5":
            fivesides()
            print("Thank you for trying our Shape Maker Program! Exiting the program...")
            break
        elif num == "6":
            sixsides()
            print("Thank you for trying our Shape Maker Program! Exiting the program...")
            break
        elif num == "7":
            sevensides()
            print("Thank you for trying our Shape Maker Program! Exiting the program...")
            break
        elif num == "8":
            eightsides()
            print("Thank you for trying our Shape Maker Program! Exiting the program...")
            break
        elif num == "0":
            print("Thank you for trying our Shape Maker Program! Exiting the program...")
            break
        else:
            print("Please enter a valid number within the range of 1-8")

        '''
        wn = t.Screen()
        moxie = t.Turtle()
        moxie.pensize(3)
        moxie.speed(0)
        # moxie.stamp()
    
        wn.exitonclick()
        '''

main()