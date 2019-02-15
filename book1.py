fin=open("Book1.txt","r")
#line = fin.readline()
#word=line.split()
#word=line.strip()
for line in fin:
 word=line.strip()
 print(word)


f=open("Book2.txt","r")
for line in f:
 word=line.strip()
 print(word)


f1=open("Book3.txt","r")
for line in f1:
 word=line.strip()
 print(word)
