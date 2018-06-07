import sys

k=input()
k=int(k)

wages= [int(i) for i in input().split()]
types_person=[int(i) for i in input().split()]

minwage1=minwage2=minwage3=100000000
i=0
while i<len(wages):
    if(types_person[i]==1):
        if(wages[i]<minwage1):
            minwage1=wages[i]

    elif(types_person[i]==2):
        if(wages[i]<minwage2):
            minwage2=wages[i]

    elif(types_person[i]==3):
        if(wages[i]<minwage3):
            minwage3=wages[i]

    i=i+1

minwage1=minwage1+minwage2

if minwage1<minwage3:
    print(minwage1)
else:
    print(minwage3)