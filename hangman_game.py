"""
Hangman Game
A simple console-based word-guessing game built in Python.
The player has 6 attempts to guess the secret word one letter at a time.
"""

import random

# List of possible secret words
word_list = ["PYTHON", "HANGMAN", "COMPUTER", "KEYBOARD", "PROGRAM"]

# Pick a random word from the list
secret_word = random.choice(word_list)

# Track guessed letters and remaining attempts
guessed_letters = []
remaining_attempts = 6

print("=" * 40)
print("Welcome to Hangman!")
print("Guess the secret word one letter at a time.")
print("You have", remaining_attempts, "attempts.")
print("=" * 40)

# Main game loop
while remaining_attempts > 0:
    # Build the current display of the word (letters guessed + asterisks)
    hidden_secret_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            hidden_secret_word += letter
        else:
            hidden_secret_word += "*"

    print("\nWord:", hidden_secret_word)
    print("Remaining attempts:", remaining_attempts)

    # Check win condition
    if hidden_secret_word == secret_word:
        print("\nYou WIN! The word was:", secret_word)
        break

    # Get and validate player input
    guess = input("Guess a letter: ").upper()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter exactly one letter.")
        continue

    # Avoid re-guessing the same letter
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Check if the guess is correct or wrong
    if guess in secret_word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        remaining_attempts -= 1
        print("Wrong guess.")

    # Check lose condition
    if remaining_attempts == 0:
        print("\nYou LOSE! The word was:", secret_word)