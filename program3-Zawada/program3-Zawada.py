# Student Name: Ethan Zawada
# Course #: CSCI 256
# Program Description: This assignment takes input from a user for a team name
# from any sport and then reads from an input file the opponents for that team.
# It will then calculate the wins, losses, and ties as well as total points
# scored by the team and the opponents. The difference of the two totals
# are then calculated and the win percentage of the team as well as what
# type of streak it is on. After all this, the data calculated is written
# to an output file given by the user.
# Time Taken to Complete: This program took me around a little over two hours
# to complete.
# Help: I did not receive any help from anyone other than using the slides
# from this course and online sources such as stackOverflow and W3Schools.


import pathlib

# get input from user for their team
yourTeam = input('What is your team? ')

# keep prompting if empty
while yourTeam == '' or yourTeam.isspace():
    yourTeam = input('Please enter a team name (non-empty): ')

# ask user for name of input file
userInputFile = input('\nWhat is the file name of your season results?'
                   '\nFor example, scores.txt: ')

# keep prompting if empty
while userInputFile == '' or yourTeam.isspace():
    userInputFile = input('Please enter an input file (non-empty): ')

# checks to see if the file exists. If not program will exit
try:
    with open(userInputFile, 'r') as inFile:
        print('Valid Input File')
except FileNotFoundError:
    print('File could not be found! Program will now terminate')
    exit()


# open said input file from user
inFile = open(userInputFile, 'r')

# ask user for name of output file
userOutputFile = input('\nWhat is the name of the file to print your results?'
                    '\nFor example, results.txt: ')

# keep prompting if empty
while userOutputFile == '' or yourTeam.isspace():
    input('Please enter an output file (non-empty): ')

# open the output file
outFile = open(userOutputFile, 'w')

# write to the output file the header with the team name
outFile.write('Season Results: ' + yourTeam + '\n\n')

# print the header
print('\nSeason Results: ' + yourTeam + '\n')

# initialize variables for calculations and comparisons
wins = 0
losses = 0
ties = 0

winStreak = 0
loseStreak = 0
tieStreak = 0

pf = 0
pa = 0

record = ''

gamesPlayed = 0

# read the first opponent name
opponent = inFile.readline().rstrip('\n')

# search the input file until there are no more opponents
while opponent != '':
    # read next two lines after an opponent for the scores of the two teams
    score1 = inFile.readline().rstrip('\n')
    score2 = inFile.readline().rstrip('\n')

    # if statements to set record of the games
    if int(score1) > int(score2):
        wins += 1
        record = 'W'
    if int(score1) < int(score2):
        losses += 1
        record = 'L'
    if int(score1) == int(score2):
        ties += 1
        record = 'T'

    # if statements to determine the streak
    if record == 'W':
        loseStreak = 0
        tieStreak = 0
        winStreak += 1
    if record == 'L':
        tieStreak = 0
        winStreak = 0
        loseStreak += 1
    if record == 'T':
        winStreak = 0
        loseStreak = 0
        tieStreak += 1

    # calculate total points of team and opponents
    pf += int(score1)
    pa += int(score2)

    # write opponent team and outcome of each games to the output file
    outFile.write('{:22}'.format(opponent) + '{:^10}'.format(score1
                    + ' - ' + score2) + '{:^3}'.format(record) + '\n')

    # print the information going to the output file
    print('{:22}'.format(opponent) + '{:^10}'.format(score1
            + ' - ' + score2) + '{:^3}'.format(record))

    # every iteration add 1 to total games played
    gamesPlayed += 1

    # read for the next opponent from the input file
    opponent = inFile.readline().rstrip('\n')

# calculate the win percentage
winPercentage = format((wins + (ties * .5)) / gamesPlayed, '.3f')

# calculate the difference
difference = pf - pa

# set the streak according to what type of streak it was last
if record == 'W':
    streak = winStreak
if record == 'L':
    streak = loseStreak
if record == 'T':
    streak = tieStreak

# write the wins, losses, ties, win percentage, totals, difference, and streak
# to the output file
outFile.write('\nW  L  T  W-PCT  PF  PA  DIFF  STRK')
outFile.write('\n=  =  =  =====  ==  ==  ====  ====')
outFile.write(f'\n{wins}  {losses}  {ties}  {winPercentage}'
              f'  {pf}  {pa}  ' + '{:^4}'.format(difference) + '  '
              + '{:^4}'.format(record + str(streak)))

# print the information that was just sent to the output file
print('\nW  L  T  W-PCT  PF  PA  DIFF  STRK')
print('=  =  =  =====  ==  ==  ====  ====')
print(f'{wins}  {losses}  {ties}  {winPercentage}'
        f'  {pf}  {pa}  ' + '{:^4}'.format(difference) + '  '
        + '{:^4}'.format(record + str(streak)))

# close the output file
outFile.close()
