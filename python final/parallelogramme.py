import turtle
import math
from trait import trait

def parallelogramme(x,y,w,d,angle,horizontal = True,c_remplissage = None):
    if c_remplissage != None:
        turtle.fillcolor(c_remplissage)
        turtle.begin_fill()
    x_decal = (d*math.cos(math.radians(angle)))
    y_decal = (d*math.sin(math.radians(angle)))
    if horizontal:    
        trait(x-w/2,y,x+w/2,y)
        trait(x+w/2,y,x+w/2+x_decal,y+y_decal)
        trait(x+w/2+x_decal,y+y_decal,x-w/2+x_decal,y+y_decal)
        trait(x-w/2+x_decal,y+y_decal,x-w/2,y)
    else:        
        trait(x,y-w/2,x+x_decal,y-w/2+y_decal)
        trait(x+x_decal,y-w/2+y_decal,x+x_decal,y+w/2+y_decal)
        trait(x+x_decal,y+w/2+y_decal,x,y+w/2)
        trait(x,y+w/2,x,y-w/2)
    if c_remplissage != None:
        turtle.end_fill()

if __name__ == "__main__":
    parallelogramme(5,4,34,34,45,False,"blue")
    turtle.exitonclick()
