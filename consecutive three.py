def cons_there(wrd):
    i=0;testcase=0

    while (i<(len(wrd)-1) and testcase<4 ):
        if wrd[i]== wrd[i+1]:
            testcase+=1
        i=i+1

    if testcase==3:
        return True
    else:return False


if  cons_there("cndjncdlsttnfsuibnsdoodspp"):
    print("hai bhai hai")