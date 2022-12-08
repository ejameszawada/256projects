import random
from random import random
from random import randint

WIN = 0
LOSE = 1

chance = randint(0, 2)

if (chance == WIN):
   print("You Win.")

elif (chance == LOSE):
   print("You Lose.")

else:
   print("It is a Draw.")