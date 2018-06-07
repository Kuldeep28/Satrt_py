import sys

fin=open("ipfil.txt")

finkey=[i for i in fin.readline().split("\n")]# here /\n will come as it will not being able to split the \n so leave that again take it and make a split of that
s=finkey[0].split(" ")
finvalues=[i for i in fin.readline().split(" ")]

print(s,"\n here its done\t",finvalues)
dic={}
for i in range(len(s)):
    dic[s[i]]=finvalues[i]          #putting the readed elemnts on the right track man iam getting god yup#

val=dic.values()
if "toto" in val:
    print("itss working")

print(dic["mart"])