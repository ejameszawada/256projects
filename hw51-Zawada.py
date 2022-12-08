# HW5.1: Student needs to define four void functions here:
#    display_nfc_east()  - to print just the 4 teams in the NFC East
#    display_nfc_north() - to print just the 4 teams in the NFC North
#    display_nfc_south() - to print just the 4 teams in the NFC South
#    display_nfc_west()  - to print just the 4 teams in the NFC West
# Then, replace (or comment out) the print statements in the "main" program below
#    to instead make calls to the newly defined functions
#    each function should print the division name and then the four teams
#    e.g., display_nfc_east()
# Then, add a fifth division with four fictional teams and a function to print those.
# Upload the .py file (e.g., hw51-lastname.py, and a proof of run
# 10 points
# Bonus for a really nice formatting

# Copy and modify this block of code for each function you want to define
#def function_name():    # change function_name (e.g., to display_nfc_east)
#   statement  # put a statement that you want. e.g., print ("NFC East\n________")
#   statement  # put a statement that you want. e.g., print ("Dallas Cowboys")
#	statement  # put another statement. e.g., print ("Washington Commanders")
#                       # add more statements as needed


#
# Original Main Program
#

# Print the names of the teams in the NFC East Division
def display_nfc_east():
    print ("Dallas Cowboys")
    print ("New York Giants")
    print ("Philadelphia Eagles")
    print ("Washington Commanders")
# You will remove (or comment out) the four lines above
# And add here a call to your function: display_nfc_east()

# Print the names of the teams in the NFC North
def display_nfc_north():
    print ("Chicago Bears")
    print ("Detroit Lions")
    print ("Green Bay Packers")
    print ("Minnesota Vikings")
# You will remove (or comment out) the four lines above
# And add here a call to your function: display_nfc_north()

# Print the names of the teams in the NFC South
def display_nfc_south():
    print ("Atlanta Falcons")
    print ("Carolina Panthers")
    print ("New Orleans Saints")
    print ("Tampa Bay Buccaneers")
# You will remove (or comment out) the four lines above
# And add here a call to your function: display_nfc_south()

# Print the names of the teams in the NFC West
def display_nfc_west():
    print ("Arizona Cardinals")
    print ("Los Angeles Rams")
    print ("San Francisco 49ers")
    print ("Seattle Seahawks")
# You will remove (or comment out) the four lines above
# And add here a call to your function: display_nfc_west()

# Here, add a call to your fifth function to display your fictional teams
def display_nfc_Zawada():
    print('Tupelo Tigerlillies')
    print('Madison Maddogs')
    print('Oxford Oxen')
    print('Austin Astronauts')

def main():
    print("NFC East\n________")
    display_nfc_east()
    print()
    print("NFC North\n________")
    display_nfc_north()
    print()
    print("NFC South\n________")
    display_nfc_south()
    print()
    print("NFC West\n________")
    display_nfc_west()
    print()
    print("NFC Zawada\n_______")
    display_nfc_Zawada()
    

main()