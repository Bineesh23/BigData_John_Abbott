import turtle

def draw_square():
        window=turtle.Screen()
        window.bgcolor("red")
        b=turtle.Turtle()
        b.shape("arrow")
        b.color("green")
        b.speed(6)
        for loo in range (0,36):
            b.right(10)
            for count in range(0,4):
                b.forward(100)
                b.right(90)
    
        window.exitonclick()
draw_square()

