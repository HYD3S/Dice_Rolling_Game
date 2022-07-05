import random
import time
repeat = True
print("Hello!")
while repeat:
    print("The Dice is Rolling...")
    time.sleep(1)
    print("The value is: ")
    print(random.randint(1,12))
    print("Do you want to roll again? Y/N ")
    repeat = "Y" in input()
else:
    print("Thanks for playing")