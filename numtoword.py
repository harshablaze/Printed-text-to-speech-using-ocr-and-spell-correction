import sys
# Function to convert a single-digit or two-digit number into words
def convertToDigit(n, suffix):
    # if `n` is zero
    if n == 0:
        return EMPTY
    # split `n` if it is more than 19
    if n > 19:
        return Y[n // 10] + X[n % 10] + suffix
    else:
        return X[n] + suffix 
# Function to convert a given number (max 9-digits) into words
def convert(n):
    # add digits at ten million and hundred million place
    result = convertToDigit((n // 1000000000) % 100, "Billion, ")
    # add digits at ten million and hundred million place
    result += convertToDigit((n // 10000000) % 100, "Crore, ")
    # add digits at hundred thousand and one million place
    result += convertToDigit(((n // 100000) % 100), "Lakh, ")
    # add digits at thousand and tens thousand place
    result += convertToDigit(((n // 1000) % 100), "Thousand ")
    # add digit at hundred place
    result += convertToDigit(((n // 100) % 10), "Hundred ")
    if n > 100 and n % 100:
        result += "and "
    # add digits at ones and tens place
    result += convertToDigit((n % 100), "")
    return result
# Python program to convert numbers to words

 
EMPTY = ""
 
X = [EMPTY, "One ", "Two ", "Three ", "Four ", "Five ", "Six ","Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
"Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
    "Seventeen ", "Eighteen ", "Nineteen "]
 
Y = [EMPTY, EMPTY, "Twenty ", "Thirty ", "Forty ", "Fifty ",
        "Sixty ", "Seventy ", "Eighty ", "Ninety "]


with open('text.txt', 'r') as file:
        words = file.read().replace('\n', ' ')
        lst = words.split()
        #print(lst)
        index=0
        for word in lst:
            try:
                i = int(word)
            except ValueError:  # if conversion to integer fails display a warning         
                #print("Warning: cannot convert to number string '%s'" % word.strip())       
                continue # skip to next line on error
            index = lst.index(word)
            lst[index]=convert(i) 
            #index += 1
        #print(lst)
        text=''
        for word in lst:
            text += word + ' '
        outFile=open('text.txt', "w")
        outFile.write(text)
        outFile.close()
        print(text)
file.close()