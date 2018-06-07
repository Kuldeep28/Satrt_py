def has_no_e(wrd, io):
    for i  in wrd:
        if(i=="e"or i=="E"):#imp note thev iterator dirctly interates as word of the string
            return  False  # keep in mind doent need parenthesis now iterat over the data structure

    return True
def percent_tller(wrd,string):
    string.replace(".","")
    string.replace("\n", "")
    string.replace(",", "")
    list=[]
    list=string.split(" ")
    print(list)
    tot=len(list)
    wrd_nothavin_e=0
    for entity in list:# you can see that we are iterating over entity of the list not the get index to acces it a major utility
        if has_no_e(entity,""):
            wrd_nothavin_e+=1
    print(wrd_nothavin_e)
    wrd_nothavin_e=(wrd_nothavin_e/tot)*100
    return wrd_nothavin_e



print(percent_tller("e","""Write a function named uses_only that takes a word and a string of letters, and
                           that returns True if the word contains only letters in the list. Can you make a sentence using only
zthe letters acefhlo"""))

