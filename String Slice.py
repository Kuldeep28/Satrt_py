#string can be slice ising [a:b]n which means from a to b exclude
#the string is going to be sliced and output is thrown
#keep in mind negative like -1 means last 1 or 1 from the end of the string

k="monty python is here to save the universe from the great ollow queen "
print(k[3:7], k[4:20], " thats how to do slicing in real world")

if "monty" in k:
    print("is here")
print(k.find("save"),k[24])#find function give the offset of the element which it is finding

#its betteer to convert all string into standard form as at comparison all acps come before all lowercase letter so keep inmind when you are doing comparison