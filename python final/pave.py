from rectangle import rectangle
import turtle
from parallelogramme import parallelogramme

def pave(x,y,w,h,d,angle,c_remplissage):
    rectangle(x,y,w,h,c_remplissage)
    parallelogramme(x,y+h,w,d,angle,True,c_remplissage)
    if angle > 90:
        parallelogramme(x-w/2,y+h/2,w,d,angle,False,c_remplissage)
    else:
        parallelogramme(x+w/2,y+h/2,h,d,angle,False,c_remplissage)

if __name__ == "__main__":
    pave(4,5,140,100,1,30,"blue")
    turtle.exitonclick()