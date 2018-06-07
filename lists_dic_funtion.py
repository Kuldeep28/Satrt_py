#in this we are using the lists function used for geeting the key value  from a dict
# thed item finctin will return the tupple of key value pairs

d={1:23,3.23:24,34:23}

print(list(d))

print(d.items())#give iterator dictitems

#Combining dict with zip yields a concise way to create a dictionary:
#>>> d = dict(zip('abc', range(3)))
#>>> print d
#{'a': 0, 'c': 2, 'b': 1}
#The dictionary method update also takes a list of tuples and adds them, as key-value pairs,
#to an existing dictionary

str1="kuldeep"
str2="parashar"
di=dict(zip(str1,str2))# this finction is actully mapping the tu[ples we get as ziped funtion as a key value pair
# so keep moving man please you are getting great at python bass code3 kar code
print(di)

for key,values in di.items():# use the iterator we get and find the key vlue pairr and do something went to do
    print(key,"is",values)