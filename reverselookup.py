def reverse_lookup(d, v):
    l=[]
    for k in d:
        if d[k] == v:
            l.append(k)
    raise ValueError  # the most important part is to raise error at the right places

#inversin the dict of alp[ha to freqency

def reverse(d):
    reversedic={}
    for key in d:
        value=d[key]
        if value not in reversedic:
            reversedic[value]=[key]#here we are making the vallue a list the frequency of occurance could be same so thier could be more that 1 person in values of reverse
        else:
            reversedic[value].append(key)
    return reversedic


tat={'k': 1, 'u': 1, 'l': 1, 'd': 1, 'e': 2, 'p': 1}
print(tat)

print(reverse(tat))#reverse is being possible by using this methoodology
#list cant be used as values ,coz they are mutable that is they can change so hah values would also change k so same key have to differnt location