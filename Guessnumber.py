import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Ask the user to guess the number
guess = int(input("Guess the number between 1 and 100: "))

# Keep asking the user to guess the number until they get it right
while guess != number:
    if guess > number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Guess the number between 1 and 100: "))

print("Congratulations! You guessed the number.")
