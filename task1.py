from string import punctuation, whitespace

book = 'origin.txt'

word = open(book)

def onlyword(word):
    total = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            total += char.lower()
    return total
        
print ("{} has {} 'words'".format(book, len([onlyword(word) for word in words])))
