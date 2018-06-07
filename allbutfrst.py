import sys

fin = [int(i) for i in input().split(' ')]
finputfile=open("ou.txt")
print(fin,"\n\n")
s=finputfile.read()

fin =[int(i) for i in s.split(' ')]                #         here we are taking input from the ou.txt file its more relaiable to see the code rarther then passing test cases
                                                   #since its a list comprehension keep in mind it comes in sqaure bracets not in paranthesis

print(fin)