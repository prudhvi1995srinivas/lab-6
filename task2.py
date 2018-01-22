import math
class rectangle():
        x=0
        y=0
p1=rectangle()
width=100
height=200

def find_center(p1,width,height):
    center=((p1.x+height/2),(p1.y+width/2))
    return center
print(find_center(p1,width,height))

class point():
    x=1
    y=2
p1=point()
dx=4
dy=8

def move_rectangle(p1,dx,dy):
    move=((p1.x+dx),(p1.x+dy))
    return move
print(move_rectangle(p1,dx,dy))

