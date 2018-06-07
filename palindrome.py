import  sys


s = "arssra"
flag = False

for i in range(len(s)):# len(obj) use to give the length of the data structure object are passed as arguments
    if s[i] == s[len(s)-i-1]:
        print("check")
        continue

    else:
        print("check1");flag=True; break#qalways remember the code after break and continue is unreachable

if( flag ):
    print("not palindrome");
else:
    print("palindrome")

index=0
while index<len(s):
    print(s[index],end="")#use end to override the print function as normally its come with new line
    index+=1


str="qweddewq"
if str==str[::-1]:             #one line version of palindrome a the third argument in slicing#
    print("\nis palincdrome")  #set the brick and from every brick 1 part is being choosen
else :
    print("\nnot palindrome")
