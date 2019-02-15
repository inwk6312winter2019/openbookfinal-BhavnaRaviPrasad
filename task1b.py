
y=open("Book1.txt","r")
for line in y:
 word=line.strip()
 word=line.split()
 print(word)

y1=open("Book2.txt","r")
for line in y1:
 word=line.strip()
 word=line.split()
 print(word)

y2=open("Book3.txt","r")
for line in y2:
 word=line.strip()
 word=line.split()
 print(word)

hist=dict()
def most_common(hist):
 t=[]
 for key,value in histitems():
  t.append((value,key))
  t.sort(reverse=true)
  return t

t=most_common(hist)
print("the most commonly used words are:")
for freq,word in t[:10]:
 print(word,freq,sep='\t')

common=set(y).intersection(Set(y1)).intersection(set(y2))
print(common)

