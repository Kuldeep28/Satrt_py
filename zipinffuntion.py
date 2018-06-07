string="kuldeepop"
tup=[1,2,5,7,8,8,9,89,90]

print(list(zip(string,tup)))# in zip function the length of the zip list is depending on the value of the shortest listt
zipped=list(zip(string,tup))

for entity,num in zipped:# that cool we are using tupple assingnment to iterate over it as we are confirmed that there
                          # would be nly 2 entities in 1 entity of the given list
    print(entity,num)

#we can use zip for and loop to traverse through three itewration at the sAme time that a great utility
def triple_triversal(ty1,ty2,ty3):
    for wr1,wr2,wr3 in zip(ty1,ty2,ty3):
        print(wr1,wr2,wr3)#here we are traversing the continous structure with same loop and i need it


st="kuldeepparasha"
st1="tanyaparashar"
st3="anitaparashar"

# enumerate is the functoin use if you wwant to traverse the structure with index and and the values at the same time









triple_triversal(st,st1,st3)