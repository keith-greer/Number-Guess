import random,sys,time

#defines the typingPrint function
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

#Generates a random number between 1 & 10
secret_number = random.randint(1, 10)

#User instructions for the game
typingPrint("Welcome to the guess the number game ")
typingPrint("I'm thinking of a number between 1 & 10. Which number am I thinking of? ")

#Variable to keep tack of the number pf guesses
guess_count = 0
max_attempts = 3

#Start a loop that allows the user to keep guessing
while guess_count < max_attempts:  # Continue until the user reaches the maximum number of attempts.
    guess = int(input("Enter your guess, loser: "))

#Adds 1 to the guess count
    guess_count += 1

#If statement to check if guess is correct
    if guess == secret_number:
       print(f"You jammy sod. Well done!! You guessed the number in {guess_count} tries.")
       break #exits loop if correct
    elif guess < secret_number:
       print("Try higher")
    else:
        print("Try lower")
else:
   print("You failed in three tries, go home and have a word with yourself.")

