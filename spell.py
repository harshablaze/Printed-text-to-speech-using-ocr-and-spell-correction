from textblob import TextBlob

#gfg = input()
infile=open('text.txt','r')
words = infile.readlines()
words = [word.strip() for word in words]
str1=''
print(words)
for word in words:
    text = TextBlob(word)
    # using TextBlob.correct() method
    text = text.correct()
    print(text)
    str1 = str1+' '+str(text)
infile.close()
outFile=open('text.txt', "w")
outFile.write(str1)
outFile.close()
