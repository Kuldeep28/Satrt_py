import sys

def check_ethere(a=0):
    fin=open("words.txt")
    line=fin.readline()
    for line in fin:           # in this we are iterating fin line by line as shown
        word = line.strip()
        if len(word)>=20:
            word.rfind()       #rfind serach the whole string for the given args and return the greatest index
            print(word)


def is_usesall(argwords,argstring2):
    a=[]
    a=argwords


#is_usesall("wex","are you aware we are here")

def useswrd(word, string="jbvdj"):
    fin=open("smart.txt")

    lene=fin.read().split(" ")
    listo=[]
    print("efnfk\n\n\n\n",lene)
    print(lene[1])

    for l in lene:
        if lene[l] not in word:
           listo.append(lene[l])

#useswrd("sgu")


def has_no_e(wrd, io):
    for i  in wrd:
        if(i=="e"or i=="E"):#imp note thev iterator dirctly interates as word of the string
            return  False  # keep in mind doent need parenthesis now iterat over the data structure

    return True

if has_no_e("gyiiuuEdbchdbk","df"):
    print("has no e")
else:
    print("has E or e")

