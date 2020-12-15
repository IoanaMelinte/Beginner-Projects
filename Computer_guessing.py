# the computer will guess the number that we provide

import random
inf= int(input("Minimum value of the number to guess: "))
sup= int(input("Maximum value of the number to guess: "))
feedback= ""
while feedback != "c":
    guess = random.randint(inf,sup)     #this variable will return the guesses of the computer
    feedback = input(f'The number {guess} is too high(h), too low(l) or correct(c): ').lower()
    if feedback == "h":
        sup = guess - 1
    elif feedback == "l":
        inf = guess+1
print (f"This is the correct number: {guess}.")



