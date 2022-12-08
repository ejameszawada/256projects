# find the users' team through input and print it back out to them
yourTeam = input('What is your team? ')
print('OK, you are the %s' % yourTeam)
# get input for the users' opponent, how much their team scored, and how much the opponent scored
opponent1 = input('\nWho is your next opponent? ')
yourScore1 = int(input('How many points did %s score vs. the %s? ' % (yourTeam, opponent1)))
opponent1Score = int(input('And how much did %s score in this game? ' % opponent1))
# get input for the users' opponent, how much their team scored, and how much the opponent scored
opponent2 = input('\nWho is your next opponent? ')
yourScore2 = int(input('How many points did %s score vs. the %s? ' % (yourTeam, opponent2)))
opponent2Score = int(input('And how much did %s score in this game? ' % opponent2))
# get input for the users' opponent, how much their team scored, and how much the opponent scored
opponent3 = input('\nWho is your next opponent? ')
yourScore3 = int(input('How many points did %s score vs. the %s? ' % (yourTeam, opponent3)))
opponent3Score = int(input('And how much did %s score in this game? ' % opponent3))
# print out the season results for each game previously entered (scores from all the games)
print('\nSeason Results: %s' % yourTeam)
print('%s \t %d - %d' % (opponent1, yourScore1, opponent1Score))
print('%s \t %d - %d' % (opponent2, yourScore2, opponent2Score))
print('%s \t %d - %d' % (opponent3, yourScore3, opponent3Score))
# print out the stats for the games played
print('\nSEASON STATS')
# calculate users' team score by adding all scores together and same with all the opponents
totalScored = yourScore1 + yourScore2 + yourScore3
totalAllowed = opponent1Score + opponent2Score + opponent3Score
# subtract to find the difference
scoreDifference = totalScored - totalAllowed
print('Total Points Scored: %d' % totalScored)
print('Total Points Allowed: %d' % totalAllowed)
print("Difference: %d" % scoreDifference)
# average points scored is to nearest whole number so we will use integer division
avgPointsScored = totalScored // 3
# avereage points allowed is to nearest tenth so we convert to float and use floating division
avgPointsAllowed = float(totalAllowed / 3)
print('Avg Points Scored: %d' % avgPointsScored)
# print to the nearest tenth
print('Avg Points Allowed: %.1f' % avgPointsAllowed)