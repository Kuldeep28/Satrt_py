def interlockgenerator( wrd1,wrd2):
    a=""
    if(len(wrd1)>=len(wrd2)):
        for i in range(len(wrd2)):
            a+=wrd1[i]+wrd2[i]

        length=len(wrd2)
        a+=wrd1[length:]
        return a
    else:
        for i in range(len(wrd1)):
            a += wrd1[i] + wrd2[i]

        length =  len(wrd1)
        a += wrd2[length:]
        return a

s=interlockgenerator("tanya","kuldeep")

print(s)
