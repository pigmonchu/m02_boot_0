import turtle
import random

turtles = []

def setup():
    global turtles
    startline = -470
    screen = turtle.Screen()
    screen.setup(960, 640)
    screen.bgcolor('lightgray')
    
    turtle_ycor = [-40, -20, 0, 20, 40]
    turtle_color = ['blue', 'red', 'purple', 'brown', 'green']
    
    for i in range(0, len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.color(turtle_color[i])
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.pendown()
        turtles.append(new_turtle)
        
def race():
    global turtles
    winner = False
    finishline = 450
    
    while not winner:
        for current_turtle in turtles:
            advance = random.randint(0,8)
            current_turtle.fd(advance)
            
            xcor = current_turtle.xcor()
            if xcor >= finishline:
                winner = True
                winner_color = current_turtle.color()
                print('Champion is', winner_color[0])
                
setup()
race()
