import math
import sys
def sqrtrt(a,x=3):
    """created to  make sqaure root so that we can do all
    i am coming al;l with all i hve any single piece its what iam """
    while True:
        print(x)
        y = (x + a / x) / 2#using newton methond we are calculating the sqaure root
        if y == x:
             break
        x = y

    return y



print(sqrtrt(4))

def sqrtrt(a,x=3):
    """created to  make sqaure root so that we can do all
    i am coming al;l with all i hve any single piece its what iam """
    while True:
        print(x)
        y = (x + a / x) / 2#using newton methond we are calculating the sqaure root
        if abs(y-x)< 0.0000001:# using this method spo taht float can also be
             break             #calculted nonterminating no can also be calculated ass tedening to 00
        x = y

    return y