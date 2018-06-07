global count
count=90

def gloabl_check():
    global count        # since its mutable we have tio say its to global so that python will update global omnen =
    count+=1
print(count)

gloabl_check()
gloabl_check()

print(count)             # evrything is good till iam coding and having foood for ebveryone whome i love

global tupe
tupe=[]
def global_checkatunmutable():    #just not geting it actually
    tupe.append("io")

print(tupe)