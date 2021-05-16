import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

file1 = open("text.txt",'r')
text = file1.read()
text = text.replace("\n",' ')
print(text)
doc = nlp(text)
#doc = nlp('Harsha')
#print([(X.text, X.label_) for X in doc.ents])
inFile=open('./input/479k-english-words/customdictionary.txt', "a+")
with open('./input/479k-english-words/customdictionary.txt') as f:
    words = f.readlines()
eng_words = [word.strip() for word in words]
#print(eng_words)
mylist = []
for X in doc.ents:
    print([(X.text,X.label_)])
    mylist.append(X.text)
print(mylist)
for word in mylist:
    if word in eng_words:
        continue
    else:
        inFile.write('\n')
        inFile.write(word)
inFile.close()
f.close()