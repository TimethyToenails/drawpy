import turtle               # allows us to use the turtle library
import keyboard

wn = turtle.Screen()        # creates a graphics window
t = turtle.Turtle()      # create a turtle named t
wn.screensize(canvwidth=10, canvheight=10, bg=None)

while(True):
    if keyboard.read_key() == "w":
        print("forward")
        t.forward(30)
    if keyboard.read_key() == "a":
        print("left")
        t.left(30)
    if keyboard.read_key() == "s":
        print("down")
        t.backward(30)
    if keyboard.read_key() == "d":
        print("right")
        t.right(30)
    if keyboard.read_key() == "c":
        print("clear")
        t.reset()
