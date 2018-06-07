t=['a','z','s','w','s']

t[1:3]=[11,22]

print(t)#this shows us that slicing can be used for compound reassingment of list
#  list slicing module is this convection
#list can contain data of different types in the same list
l=[["kuii","hfjhsfjh",89],45454,78.2323]#this list has  entites of differnt data types also it shows multiple list assingnment NESTED

l=["kuldeep","tanya","maa"]+l

print(l)

l.extend(l)##this is going to give same effect as + give the concatination could be done by this only
il=["a","c","d","s"]
print(il.sort())#return null its a disappointing result dont you think



#total will act as accumulator
s=[11,2,12]
print(sum(s))#keep this in mind that s will add only if the lisyt contain same object inside the list otherwise error
s="jfkdjb"

def Capitalse(a):
    if(len(a)==0):
        print("no element you bull sit")
        return
    else:
        for liste in a:
            if type(liste) == list:
                for string in liste:
                   string= string.capitalize()
                   print(string.capitalize())
            else :
                liste=liste
                print(liste.capitalize())


    return a


liste=[["kuldeep","parashar"],"tanya ","parashar",["rajeev","parashar"]]

#las=Capitalse(liste)


#print(las)
d="kjeknc"
print(d.capitalize())


def nested_sum(a):
    accumulate=0
    if(len(a)==0):
        print("no element you bull sit")
        return
    else:
        for liste in a:
            if type(liste) == list:
                for string in liste:
                   accumulate+=string
            # accumulate+=string


    return  accumulate

a=[22,[2,34,43,3,454,3],545,[4,34,343,5]]
print(nested_sum(a))

#deleteion methodology in python
# bascially we are going to usee:
#del(),dont need the deleted obj
#pop()no idex delete  the last one and pop it up means give arguments
#remove("entities") use when you doesnt know that after what is th index use this directly put the elemnt as argument
#

listcheck=[1,2,2,2,1,87,78,646,454,21]

listcheck.remove(2)
print(listcheck)

listcheck.remove(2)#keep in acount that only one elemnt is going to be removed as one remove is its have copy
print(listcheck)

listcheck.remove(2)
print(listcheck)

print(listcheck.pop(6))

print(listcheck)# all the above operator are going to reduce the size of  the lists