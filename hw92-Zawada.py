# instantiate the dictionary
destiny = {'Warlock': ['Sunsinger', 'Voidwalker', 'Stormcaller'],
           'Titan': ['Sunbreaker', 'Defender', 'Striker'],
           'Hunter': ['Gunslinger', 'Nightstalker', 'Arcstrider']}

# brief description of the game, for a slight understanding
print('In the game Destiny 2, there are 3 unique classes the player'
      '\ncan choose from. Within these 3 classes there are also, 3'
      '\nsubclasses to make the gameplay fresh each time you play.')

# get the keys of the dictionary and print them to the screen
classes = destiny.keys()
print('\nThe 3 classes in Destiny 2 are: ')
for character in classes:
    print(character)

# print all the values of each key
print('\nHere are all the subclasses in the game: ')
subClasses = destiny.values()
for subclass in subClasses:
    print(subclass)

# print specifically the warlock subclasses
war_subs = destiny['Warlock']
print('\nThe subclasses of Warlocks are: ')
for subs in war_subs:
    print(subs)

# specifically the titan subclasses
titan_subs = destiny['Titan']
print('\nThe subclasses of Titans are: ')
for subs in titan_subs:
    print(subs)

# specifically the hunter subclasses
hunter_subs = destiny['Hunter']
print('\nThe subclasses of Hunters are: ')
for subs in hunter_subs:
    print(subs)

# prompt the user to pick one of the classes
pick = input('\nThe Warlock is a magic character, the Titan is a brawler,'
      '\nand the Hunter is quick and agile. Which class would you choose?'
             '\n(Warlock, Titan, Hunter): ')

# if the user does not pick a correct option, it will continue to ask
while pick != 'Warlock' and pick != 'Titan' and pick != 'Hunter':
    pick = input('Enter only Warlock, Titan, or Hunter: ')

# pop the user's pick out the dictionary
chosen = destiny.pop(pick)

# print what the user chose and it's respective subclasses
print('\nYou chose ' + pick + ' and your subclasses are: ')
for subs in chosen:
    print(subs)

# print the other two classes in the dictionary now that one has been popped
print('\nThe other two classes you could have picked are: ')
for classes in destiny:
    print(classes)