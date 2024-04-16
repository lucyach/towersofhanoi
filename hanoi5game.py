from turtle import *
import turtle

pole1_main = []
pole2_main = []
pole3_main = []
clearscreen()


def newGame():
    # initialize poles
    pole1_main = [5, 4, 3, 2, 1]
    pole2_main = []
    pole3_main = []

    print("pole1: " + str(pole1_main))
    print("pole2: " + str(pole2_main))
    print("pole3: " + str(pole3_main))
    
    # begin game
    drawPoles()

    # draw rings
    y_suggest = 0
    for i in range(0, len(pole1_main)): # pole 1
        drawRing(pole1_main[i], 1, i, y_suggest)
        y_suggest += pole1_main[i]*10
    y_suggest = 0
    for i in range(0, len(pole2_main)): # pole 2
        drawRing(pole2_main[i], 2, i, y_suggest)
        y_suggest += pole2_main[i]*10
    y_suggest = 0
    for i in range(0, len(pole3_main)): # pole 3
        drawRing(pole3_main[i], 3, i, y_suggest)

    move(pole1_main, pole2_main, pole3_main)

def move(pole1, pole2, pole3):
    # choose the ring off of the pole with pole number
    selection = input("pick a pole to take the top ring off of: 1,2,3: ")
    selection = int(selection) # to find ring on pole
    selectedPole = selection # save the selected pole for later
    if (selection == 1):
        selection = pole1[len(pole1)-1]
    elif (selection == 2):
        selection = pole2[len(pole2)-1]
    elif (selection == 3):
        selection = pole3[len(pole3)-1]
    else:
        print("Not a pole. Pick from 1,2,3")
        move()
    # print("your selection is the ring "+ str(selection))
    if (selection == 0):
        print("No rings on that pole. Pick again.")
        move()
    else: # now choose the pole to move the selected ring to with the pole number
        movingTo = 0
        movingTo = input("which pole would you like to move ring "+ str(selection) +" to? Pick 1,2,3: ")
        movingTo = int(movingTo)
        poleMovingTo = ""
        if (movingTo == 1):
            poleMovingTo = pole1
        if (movingTo == 2):
            poleMovingTo = pole2
        if (movingTo == 3):
            poleMovingTo = pole3
        elif (movingTo != 1 and movingTo != 2 and movingTo != 3):
            print("Not a pole. Pick from 1,2,3")
            move(pole1, pole2, pole3)

        # update player
        print("you are moving ring " + str(selection) + " to pole " + str(movingTo) + " which has ring " + str(poleMovingTo) + " on it")
        
        # check if the ring can be moved
        if (len(poleMovingTo)> 0 and poleMovingTo[(len(poleMovingTo)-1)] < selection):
            print("You can't put a larger ring on a smaller one. Pick again.")
            move(pole1, pole2, pole3)
        else:
            poleMovingTo.append(selection) # add to new pole
            
            # remove from previous pole
            if selectedPole == 1:
                pole1 = pole1[:-1]
            if selectedPole == 2:
                pole2 = pole2[:-1]
            if selectedPole == 3:
                pole3 = pole3[:-1]


            # update main poles
            if poleMovingTo == pole1:
                pole1 = poleMovingTo
            if poleMovingTo == pole2:
                pole2 = poleMovingTo
            if poleMovingTo == pole3:
                pole3 = poleMovingTo

            # update player
            print("Move successful")
            print("pole1: " + str(pole1))
            print("pole2: " + str(pole2))
            print("pole3: " + str(pole3))
            
            drawPoles()

            # draw rings
            y_suggest = 0
            for i in range(0, len(pole1)): # pole 1
                drawRing(pole1[i], 1, i, y_suggest)
                y_suggest += pole1[i]*10
            y_suggest = 0
            for i in range(0, len(pole2)): # pole 2
                drawRing(pole2[i], 2, i, y_suggest)
                y_suggest += pole2[i]*10
            y_suggest = 0
            for i in range(0, len(pole3)): # pole 3
                drawRing(pole3[i], 3, i, y_suggest)

            move(pole1, pole2, pole3)

def drawPoles():
    clearscreen()
    hideturtle()
    turtle.speed(0)
    # draw poles
    penup()
    goto(-300, 0)
    pendown()
    forward(600)
    penup()

    goto(-200, 0)
    pendown()
    goto(-200, 200)
    penup()

    goto(0, 0)
    pendown()
    goto(0, 200)
    penup()

    goto(200, 0)
    pendown()
    goto(200, 200)
    penup()

    
def drawRing(num, pole, loc, y_pos):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    if num == 1:
        t.fillcolor("red")
    if num == 2:
        t.fillcolor("orange")
    if num == 3:
        t.fillcolor("yellow")
    if num == 4:
        t.fillcolor("green")
    if num == 5:
        t.fillcolor("blue")

    x = 0
    y = 0
    if pole == 1:
        x = -200
    if pole == 2:
        x = 0
    if pole == 3:
        x = 200

    y = y_pos + loc
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill() 
    t.circle(num*5)
    t.end_fill()
    t.penup()


newGame()