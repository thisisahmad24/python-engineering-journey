# A Simple Number Guessing Game
secretNumber = 7
print('Welcome to the Guessing Game!')

while True:
    guess = input('Guess a number between 1 and 10: ')
    guess = int(guess)

    if guess < secretNumber:
        print('Too low! Try again.')
    elif guess > secretNumber:
        print('Too high! Try again.')
    else:
        print('Congratulations! You guessed the number!')
        break
