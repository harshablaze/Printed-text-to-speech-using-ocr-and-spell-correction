import re
text = 'my name is chandrasekhar'
text = """ hi, balu, @@ my name is harsha. i am from vizag and my brother name is harshablaze.
 welcome to anits iam from nallajerla city gollagudem locality west godavari district :ap Andhra"""

input_file = open("text.txt",'r')
text = input_file.read()
text = text.replace('\n',' ')
raw_text = text
raw_text = raw_text.replace('\n',' ')
raw_text = re.sub('\s+', ' ', raw_text)
text = text.replace(',','')
text = re.sub('[^0-9a-zA-Z.]+',' ',text)
text = re.sub('\s+',' ',text)
print(text)

#taking existing dictionary words to avoid as native words
native = ''
with open('./input/479k-english-words/dictionary1.txt') as f:
    words = f.read().replace('\n',' ')
native += words
with open('./input/479k-english-words/customdictionary.txt') as f:
    words = f.read().replace('\n',' ')
native += words
with open('./input/479k-english-words/indian_names.txt') as f:
    words = f.read().replace('\n',' ')
native += words
with open('./input/479k-english-words/indian_cities.txt') as f:
    words = f.read().replace('\n',' ')
native += words
with open('./input/479k-english-words/indian_states.txt') as f:
    words = f.read().replace('\n',' ')
native += words
with open('./input/479k-english-words/english_names.txt') as f:
    words = f.read().replace('\n',' ')
native += words
f.close()

#detecting names
names = []
names = re.findall(r"name is [a-z]*",text.lower())
names.extend(re.findall(r'hi [a-z]*',text.lower()))
names.extend(re.findall(r'from [a-z]*',text.lower()))
names.extend(re.findall(r'welcome to [a-z]*',text.lower()))
names.extend(re.findall(r'called [a-z]*',text.lower()))
names.extend(re.findall(r'left for [a-z]*',text.lower()))
names.extend(re.findall(r'going to [a-z]*',text.lower()))
names.extend(re.findall(r'called [a-z]*',text.lower()))
names.extend(re.findall(r'heading [a-z]*', text.lower()))
names.extend(re.findall(
    r'([a-z]* locality|[a-z]* city|[a-z]* town|[a-z]* village|[a-z]* district)', text.lower()))
names.extend(re.findall(r':\s*[a-z]*',raw_text.lower()))
names.extend(re.findall(r' [A-Z][a-z]*', text))
names.extend(re.findall('\\b[a-z][a-z.&]{2,7}\\b', text.lower()))
#print(names)
detected_names = ''

for name in names:
    detected_names += ' '+name
list1 = detected_names.split(' ')
detected_names = ''
#print(list1)
for name in list1:
    if name in native:
        #print(name)
        continue
    else:
        detected_names +=' '+name

detected_names = re.sub('\s+', ' ', detected_names)
detected_names = re.sub('[^0-9a-zA-Z. ]+', '', detected_names)
print(detected_names[1::])
mylist = detected_names.split(' ')
with open('./input/479k-english-words/customdictionary.txt') as f:
    words = f.readlines()
native = [word.strip() for word in words]
inFile = open('./input/479k-english-words/customdictionary.txt','a+')
for word in mylist:
    if word in native:
        continue
    else:
        inFile.write('\n')
        inFile.write(word)
inFile.close()
