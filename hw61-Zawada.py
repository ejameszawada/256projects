# instantiate number, word, and file names
FAV_NBR = 24
FAV_WORD = "noble"
f = "favoritewords.txt"
of = "hw61-Zawada.out"

## Open the input file
f = open('/Users/Ethan/Desktop/CSCI256/favoritewords.txt', 'r')
## Open the output file
of = open('hw61-Zawada.out', 'w')

# for loop iterating until my number and writing to file
for nbr in range(0, FAV_NBR+1):
    print(nbr)
    of.write(str(nbr) + '\n')

# write my favorite number to the file
print('My favorite number was:', nbr)
of.write("My favorite number was: " + str(nbr))

# read for the first word from the input
word = f.readline()

# searching for word until found
searching = True
while searching:
    # if the word is a match it will write to file and end loop
    if word.rstrip() == FAV_WORD:
        print('My favorite word was: ' + word)
        of.write('\nMy favorite word was: ' + word)
        searching = False
    # otherwise read again
    else:
        word = f.readline()

# read the next word after mine
nextWord = f.readline()
# print that next word
print('The next word in the file is: ' + nextWord)
of.write('The next word in the file is: ' + nextWord)
# close the output file
of.close()
