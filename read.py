
words=''
with open('text.txt', 'r') as file:
    words = file.read().replace('\n', '')
print(words)
