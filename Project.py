import turtle
wn=turtle.Screen()
turtle.bgcolor("white")
star=turtle.Turtle()
turtle.shape()
    
def aries():
    star.left(45)
    star.stamp()
    star.forward(50)
    star.left(35)
    star.stamp()
    star.forward(100)
    star.right(95)
    star.stamp()
    star.forward(100)
    star.right(45)
    star.stamp()
    star.forward(20)
    star.stamp()

def taurus():
    star.right(35)
    star.stamp()
    star.forward(100)
    star.left(35)
    star.stamp()
    star.forward(20)
    star.stamp()
    star.forward(20)
    star.stamp()
    star.left(120)
    star.forward(40)
    star.left(20)
    star.stamp()
    star.right(20)
    star.forward(40)
    star.left(20)
    star.forward(50)
    star.stamp()
    star.forward(100)
    star.stamp()
    star.penup()
    star.backward(260)
    star.left(40)
    star.forward(50)
    star.left(180)
    star.right(20)
    star.pendown()
    star.forward(50)
    star.stamp()
    star.forward(100)
    star.stamp()
    
def gemini():
    star.left(45)
    star.stamp()
    star.forward(50)
    star.right(50)
    star.stamp()
    star.forward(35)
    star.right(35)
    star.forward(75)
    star.left(35)
    star.stamp()
    star.forward(100)
    star.left(15)
    star.stamp()
    star.forward(45)
    star.stamp()
    star.penup()
    star.backward(45)
    star.right(125)
    star.pendown()
    star.forward(55)
    star.right(25)
    star.stamp()
    star.forward(25)
    star.left(45)
    star.stamp()
    star.forward(45)
    star.stamp()
    star.penup()
    star.backward(45)
    star.pendown()
    star.right(100)
    star.forward(60)
    star.stamp()
    star.forward(30)
    star.stamp()
    star.left(20)
    star.forward(50)
    star.left(100)
    star.right(160)
    star.stamp()
    star.forward(90)

def cancer():
    star.right(80)
    star.stamp()
    star.forward(70)
    star.right(20)
    star.stamp()
    star.forward(20)
    star.stamp()
    star.right(20)
    star.forward(40)
    star.stamp()
    star.penup()
    star.backward(40)
    star.left(80)
    star.pendown()
    star.forward(50)

##def leo():
    
month=input("What month were you born?:")
day=int(input("What day of the month were you born?:"))

if month=="march" or "april":
    if month=="april" and day<=19:
        aries
    if month=="march" and day>=21:
        aries

elif month=="may" or "april":
    if month=="april" and day>=19:
        taurus
    if month=="may" and day<=20:
        taurus

elif month=="may" or "june":
    if month=="may" and day>=21:
        gemini
    if month=="june" and day<=20:
        gemini

elif month=="june" or "july":
    if month=="june" and day>=21:
        cancer
    if month=="july" and day<=22:
        cancer

elif month=="july" or "august":
    if month=="july" and day<=23:
        leo
    if month=="august" and day>=22:
        leo
wn.mainloop()
