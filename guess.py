import random
import math

def guessing_game():
    lower = int(input("Enter a lower bound: "))
    upper = int(input("Enter an upper bound: "))
    x = random.randint(lower, upper)
    calc = math.log(upper - lower + 1, 2)
    print("\nYou've only ", round(calc), " chances to guess the integer!\n")

    count = 0
    
    while count < calc:
        count += 1
        guess = int(input("Guess a number: "))
        if x == guess:
            print("Congratulations you did it in ", count, " try/tries")
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")
    if count >= calc:
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")