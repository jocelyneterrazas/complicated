import math
from turtle import *


##Law of Cosine

def myTriangle():
    firstSide = int(input("Please give me the first side length:"))
    secondSide = int(input("Please give me the second side length:"))
    firstAngle = int(input("Please give me the third angle:"))


    thirdSide = (pow(firstSide,2) + pow(secondSide,2)) - ((2)*(firstSide)*(secondSide)*(math.cos(math.radians(firstAngle))))
    thirdSide1 = pow(thirdSide,0.5)

    secondAngle= math.acos(((pow(secondSide,2)) - (pow(firstSide,2)) - (pow(thirdSide1,2)))/ ((-2)*(firstSide)*(thirdSide1)))
    secondAngle1= math.degrees(secondAngle)

    thirdAngle = 180 - firstAngle - secondAngle1

    print(thirdAngle)
    ##print(secondAngle1)
    ##print(thirdSide1)

    ## TURTLE DRAWING ##
    jocelyne = Turtle()
    jocelyne.goto(0,0)
    jocelyne.down()
    jocelyne.forward(firstSide)
    jocelyne.left(180-thirdAngle)
    jocelyne.forward(secondSide)
    jocelyne.left(180-firstAngle)
    jocelyne.forward(thirdSide1)

    print("First Angle:")
    print(firstAngle)
    print("Second Angle:")
    print(secondAngle)
    print("Third Angle:")
    print(thirdAngle)

if __name__ == "__main__":
        myTriangle()
