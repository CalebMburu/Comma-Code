import sys

def listToString(words):
    try:
        newString = ''
        for i in range(len(words) - 1):
            newString += words[i] + ', '
        newString += 'and ' + words[-1]
        print(newString)

    except IndexError:
        sys.exit()

fruits = ['apples', 'bannans', 'tofu', 'cats']

listToString(fruits)
