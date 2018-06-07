def histogram(string):# the best way to find that how many times it has came
    d={}              # since it uses hashing so com[plexity doesnt rise that much
    for c in string:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d

str="kuldeep"
op=histogram(str)
opget=op.get('z',"sry")#this get functios are going to give the valuse if key is found otherwise they give the default value given as second args to the function
print(op,opget)