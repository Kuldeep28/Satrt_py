import sys
import math


def circle_area(x1,y1,x2,y2):
    radius=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return math.pi*radius**2


output=circle_area(0,0,7,0)

print(output)

# an example of bolean function are going to
# came be ready to tackle it there is something we all are hoping to create the will is inside me to tackle it

def is_factor(a,d):
    if(a%d==0):
        return True
    else:
        return False

if is_factor(22,2):
    print("2 is a factor of 22")