def tupple_mulitupl_args(*args):    #if you want to send multiple values use *args it stores the argments inthe form of tupple which can easily be extracted
    print(args)


s=("a","x","1","we","are ttanu")

tupple_mulitupl_args(s)

#scatterning the continious data and sending it aftern disisiation is what scatrer do when a fx is called jusdt put *in front o a datastrucre so that it would be split
a=[23,3]
print(divmod(*a))#this code will be error prone while is so put star infron of the list 2 argument are being sent to the function
a,c="kuldeep parashar".split(" ")#tupple assingnment to a,c split and given ta a,c
print(a,c)

summx=max(5,23,89,78)# max and min funtion can take variable no of arguments yeah work load reduced man love you python

print(summx)

