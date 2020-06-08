import random
print("Dice Rolling Simulator.\nPress 'Y' to Roll Dice and 'N' to stop.\n")
while True:                     # while 1
    ch = input("Roll Dice ?\n")
    if ch == 'Y' or ch == 'y':
        x = random.randint(1, 6)
        print(x)
    elif ch == 'N' or ch == 'n':
        break
    else:
        break
