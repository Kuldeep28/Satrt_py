
s="melon"
newstr=""
for i in range(len(s)):

   newstr+=chr(ord(s[i])+26)            #in python we chr is used to print or convert asci tpo the respective character asociated

fin=open('words.txt')#using it to open a text file the file name given as string as ittt is bing searched in directory
a = fin.readline()
i=0
while i <10:   #use the strip() fx to remove the new line charcter compint in read command
     if len(a)>=20:
         print(a)

