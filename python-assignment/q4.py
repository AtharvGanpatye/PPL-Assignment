import random
n = random.randint(0, 50)
x = int(input("Guess a number between 1 and 50 :\n"))
while True:
    if n < x:
        print("The number is less than ", x)
        x = int(input("Guess again :\n"))
    elif n > x:
        print("The number is greater than ", x)
        x = int(input("Guess again :\n"))
    else:
        print("\nCongratulations !\nCorrect Guess !!")
        break
