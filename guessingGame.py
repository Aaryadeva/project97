import random
print("Number guessing game")
randomNumber = random.randint(1, 9)
chances = 0
print("Guess a number between 1 and 9: ")

while chances < 5:
    guessedNumber = int(input("Enter your guess: "))
    if guessedNumber == randomNumber:
        print("You guessed the correct number")
        break
    elif guessedNumber < randomNumber:
        print("Guess a higher number than", guessedNumber)
    else:
        print("Guess a lower number than", guessedNumber)
    chances += 1

if not chances < 5:
    print("You guessed incorrectly the number was ", randomNumber)