import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

#for j in range(0,24):
    for i in range(0, 4):
        brad.forward(100)
        brad.right(90)
    #brad.right(15)

   
        
    window.exitonclick()

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
    
draw_square()
#draw_circle()
#draw_triangle()
