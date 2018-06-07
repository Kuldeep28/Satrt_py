def is_anagram(wrd1,wrd2):
    counter=0
    if len(wrd1)==len(wrd2):
       i=0
       for i in range(len(wrd1)):
           for j in range(len(wrd2)):
               if(wrd1[i]==wrd2[j] and nonrecurent(wrd1[i])):
                   counter+=1     #by using thi logic we have made a simple hypothesis that waht it is
                                  #by k
       if (counter%len(wrd2)==0):
           return True
       else:
           return False
    else:
        return False



s1="kuldep"
s2="ludekp"

if is_anagram(s1,s2):
    print("the both words are anagram")
else:
    print('these are not anagram')

def nonrecurent(wrd):
    wrd=""
    wrd.index()