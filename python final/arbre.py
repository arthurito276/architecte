import turtle
from rectangle import rectangle

def arbre(x,y,h,w):
    rectangle(x,y,7.5,h,"brown")
    rectangle(x,y+h-5,w,w,"forest green")

if __name__ == "__main__":
    arbre(34,34,30,25)
    turtle.exitonclick()