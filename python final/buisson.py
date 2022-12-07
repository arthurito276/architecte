from rectangle import rectangle
import turtle

def buisson(x,ySol,w):
    turtle.fillcolor("forest green")
    turtle.begin_fill()
    rectangle(x,ySol,w,20)
    turtle.end_fill()

if __name__ == "__main__":
    buisson(6,0,25)
    turtle.exitonclick()