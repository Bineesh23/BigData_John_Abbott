import turtle
def draw_square():
        window=turtle.Screen()
        window.bgcolor("red")
        b=turtle.Turtle()
        b.shape("arrow")
        b.color("green")
        b.speed(6)
        for count in range(0,4):
            b.backward(200)
            for loo in range (0,4):
                    b.backward(100)
                    b.right(90)
            b.right(90)
    
        window.exitonclick()
draw_square()

