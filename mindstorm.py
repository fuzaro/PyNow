import turtle

def draw_square(some_turtle):
    for i in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(0,36):
        draw_square(brad)
        brad.right(10)

   
        
    window.exitonclick()

draw_art()

#def draw_circle():
#    window = turtle.Screen()
#    window.bgcolor("yellow")
#    
#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("red")
#    angie.circle(100)
#    window.exitonclick()

#def draw_triangle():
#    window = turtle.Screen()
#    window.bgcolor("green")
#    
#    triny = turtle.Turtle()
#    triny.shape("arrow")
#
#    for i in range(0, 3):
#        triny.forward(100)
#        triny.right(120)

#    window.exitonclick()
    
#draw_square()
#draw_circle()
#draw_triangle()
