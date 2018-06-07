def permannt(li):
    li=li.append(2)# append is going to modify the list so graet to do that to make permanent effect


def notso_permanent(lo):
    r=lo+[2,3,32,2]#not modifying the list create a new list
    print("isede the function new list is created",lo)


li=[1,25,8,4,33,32,2]
permannt(li)
notso_permanent(li)
print(li)