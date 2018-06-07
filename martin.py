#since imutable objects cant be used as key in dictionary
#keep it moving

di={("kuldeep","parashar"):8602037721,("rajiv","parashar"):8602058205}

for namefirst,values in di.items():
    a,b=namefirst               # spliting of tupple can be used for this
    print(a,b,"no is",values)
t1=(1,23,43,23)
t2=(1,56,43,23)

if t1<t2:
    print("t1 is greater")#m this will check first if tie than go to the next