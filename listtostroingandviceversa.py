#use list(s) it convert into list of char to the given stringe
#if wanto split in word wise format that its ok

s="kuldeep is a hgreat nerd nunch guide here to get how"
li=list(s)
print(li)# this will generate a list of charachters so not taht effective change it

li=s.split(" ")
print(li)# this will print the list as word seperated than why to use this??

delimeter=" "
delimeter.join(li)# delimeter is  a key word actually use it to form a stringg from the list no other
                  #aarguments are not going to work keep in mind

print(s)


a="banana"
b="banana"#this python automatically maps the object once created to the differnt pointer asking for same object
if a is b :
    print("are identical man they are ")
else:
    print("they are not identical")

a=[11,2,3]
b=[11,2,3]
if a is b :
    print("are identical man they are ")# so not the same therfore else condition will ber true
else:                                   #for the case of single string it is true i dont know why
    print("they are not identical")
    