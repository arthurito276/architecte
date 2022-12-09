import turtle
import math
from trait import trait

def parallelogramme(x,y,w,h,angle_d,angle_p,c_remplissage = None):
    if c_remplissage != None:
        turtle.fillcolor(c_remplissage)
        turtle.begin_fill()
    x_pente = w*math.cos(math.radians(angle_p))
    y_pente = h*math.sin(math.radians(angle_p))
    
    x_decal = (h*math.cos(math.radians(angle_d)))
    y_decal = (h*math.sin(math.radians(angle_d)))
    point_a = [x+x_pente/2,y-y_pente/2]
    point_b = [point_a[0]+x_decal,point_a[1]+y_decal]
    point_c = [point_b[0]-x_pente,point_b[1]+y_pente]
    point_d = [point_c[0]-x_decal,point_c[1],-y_decal]
    coo = [point_a,point_b,point_c,point_d]

    trait(point_a[0],point_a[1],point_b[0],point_b[1])
    trait(point_b[0],point_b[1],point_c[0],point_c[1])
    trait(point_c[0],point_c[1],point_d[0],point_d[1])
    trait(point_d[0],point_d[1],point_a[0],point_a[1])
    
    
    
    
    '''if horizontal:    
        trait(x-w/2,y,x+w/2,y)
        trait(x+w/2,y,x+w/2+x_decal,y+y_decal)
        trait(x+w/2+x_decal,y+y_decal,x-w/2+x_decal,y+y_decal)
        trait(x-w/2+x_decal,y+y_decal,x-w/2,y)
    else:        
        trait(x,y-w/2,x+x_decal,y-w/2+y_decal)
        trait(x+x_decal,y-w/2+y_decal,x+x_decal,y+w/2+y_decal)
        trait(x+x_decal,y+w/2+y_decal,x,y+w/2)
        trait(x,y+w/2,x,y-w/2)'''
    if c_remplissage != None:
        turtle.end_fill()

if __name__ == "__main__":
    parallelogramme(5,4,34,34,45,90,"blue")
    turtle.exitonclick()
