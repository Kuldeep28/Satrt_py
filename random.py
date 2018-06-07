def binarysort(array,search):
    a=len(array)
    if(array[a/2])==search:
        return (a/2)
    elif(array[a/2]>search):
        return array[:(a/2)+1]
    elif(array[a/2]<search):
        return array[(a/2)+1:]



l=[1,2,3,4,5,6,7,8,9]
print(binarysort(l,5))