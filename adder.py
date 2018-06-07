
def sum(indx,listget):
    if (indx-1)>-1:
        return (listget[indx-1]+listget[indx])
    else:
        return listget[indx]

l=[1,2,4,3,1,2,4,4,12]

for i in range(len(l)):
    l[i]=sum(i,l)

print(l)
