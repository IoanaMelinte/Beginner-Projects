# the computer has a secret number that we have to guess
import random
guess = int()
x = int(input("Maximum value of the number to guess: "))
random_num= random.randint(1, x)
while guess != random_num:
    try:
        guess = int(input(f"Write a number between 1 and {x}: "))
        if guess < random_num:
            print (f"{guess} is too low, guess again!")
        elif guess > random_num:
            print(f"{guess} is too high, guess again!")
    except ValueError:
        print("Please write a number not a character!")
print(f"{guess} is the number!")
