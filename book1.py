fin=open("Book1.txt","r")
#line = fin.readline()
#word=line.split()
#word=line.strip()
for line in fin:
 word=line.strip()
 word=line.split()
 print(word)


#f=open("Book2.txt","r")
#for line in f:
 #word=line.strip()
 #print(word)


#f1=open("Book3.txt","r")
#for line in f1:
 #word=line.strip()
 #print(word)

def count_the_article(fin):
  wordDict = {}
  for line in fin:
    wordList = fin.split()
    for word in wordList:
      if word in wordDict: wordDict[word] += 1
      else: wordDict[word] = 1
  return wordDict

def unique_words():
 for letter in word:
  if letter==letter:
   return letter
  else:
   print(word)
unique_words()

def sorted_words():
 for line in fin:
  line.sort(reverse=True)
 print('sorted lines in the book')
print(sorted_words())

def character_word_count():
 string=string.lower().split()
 dict={}
 for item in string:
  dict[item]=item.count(item)
 print(dict)
character_word_count()

with open("Book1.txt","r") as fin:
 f=fin.read()
count=0
string=('a','e','i','o','u')
for word in fin:
 if word[0]==string:
  count=count+1
  return count
print(word) 

