from rectangle import rectangle
import turtle

def buisson(x,ySol,w):
    rectangle(x,ySol,w,20,"forest green")

if __name__ == "__main__":
    buisson(6,0,25)
    turtle.exitonclick()