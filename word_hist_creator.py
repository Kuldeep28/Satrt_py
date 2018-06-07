#word density founder in python op as a dixct giving name and index

import string

def process_file(filename):
    hist=dict()
    fp=open(filename)
    for line in fp:
        process_line(line,hist)
    return hist

def process_line(line,hist):
    line=line.replace('-',' ')

    for word in line.split():#check this doudt here also no args are been given to this split fx
        word=word.strip(string.punctuation+string.whitespace)
        word=word.lower()

        hist[word]=hist.get(word,0)+1#this dict.get() return the value or give the default argument which is passed as second args

hist=process_file("paragraph.txt")
print(hist.items())
a=[]

s=dict()
for key,values in hist.items():
    a.append(key)

a.sort()
print(a)