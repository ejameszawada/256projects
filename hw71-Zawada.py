# Ethan Zawada
# CSCI 256 Homework 7.1

# create a list of teams
teams = ['Faclons', 'Panthers', 'Buccaneers']

print(', '.join(teams))

# ask for the missing team from said list
missingTeam = input('What team is missing from the list? ')

# if the user gets it incorrect it will ask again until it is right
while missingTeam != 'Saints':
    missingTeam = input('Try Again! '
                          'What team is missing from the list? ')

print('Correct!')
# insert the correct missing team and print
teams.insert(3, missingTeam)
print(', '.join(teams) + ' are all the teams in the NFC South')

# mutate the list to change the teams and print the result
teams = ['Giants', 'Eagles', 'Cowboys', 'Commanders']
print('\nNFC east: ' + ', '.join(teams))

# ask how many teams are in this division
num = input('How many teams are in the NFC east? ')

# compare the answer to the length of the list
if int(num) == len(teams):
    print('Correct again!')
else:
    print('Sorry, there are 4 teams')

# create a tuple of the alphabet
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

print('\n' + ', '.join(alphabet))

# ask user for first letter
first = input('What is the first letter of the alphabet? ')

# compares to first letter
if first.lower() == min(alphabet):
    print('Correct, the first letter is ' + min(alphabet))
else:
    print('Sorry, the first letter is ' + min(alphabet))

# compares to last letter
last = input('\nWhat is the last letter of the alphabet? ')

# compares to last letter
if last.lower() == max(alphabet):
    print('Correct, the last letter is ' + max(alphabet))
else:
    print('Sorry, the last letter is ' + max(alphabet))


# ask user a question
backward = input('\nCan you say the alphabet backwards? ')

# the program will print the tuple reversed no matter what the user answers
if backward.lower() == 'yes':
    print('Wow! That is cool. So can this program!')
    print(', '.join(alphabet[::-1]))
elif backward.lower() == 'no':
    print('Hey no worries. I can\'t either, but this program can')
    print(', '.join(alphabet[::-1]))
else:
    print('Not sure what that means, but this program can')
    print(', '.join(alphabet[::-1]))
