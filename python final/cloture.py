import turtle
from rectangle import rectangle

def cloture(x,y_sol,w):
    turtle.pencolor("peru")
    rectangle(x,y_sol+10,w,5,"peru")
    rectangle(x,y_sol+25,w,5,"peru")
    nb_planche = w // 6
    turtle.pencolor("black")
    for x_planche in range(x-w//2,x+w//2+1,10):
        rectangle(x_planche,y_sol,5,35,"peru")



if __name__ == "__main__":
    cloture(0,0,80)
    turtle.exitonclick()