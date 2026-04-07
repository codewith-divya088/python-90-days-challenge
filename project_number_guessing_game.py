import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print("Congratulations! You guessed it right 🎉")
        break
