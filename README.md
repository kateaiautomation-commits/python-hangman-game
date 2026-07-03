# 🎮 Hangman Game (Python)

A simple console-based Hangman game built in Python as part of a Gen AI for Software Development course. The player has 6 attempts to guess a secret word one letter at a time.

## Features

- Randomly selects a secret word from a word list
- Tracks and displays guessed letters using a masked word (e.g., `*****A*`)
- Validates user input (must be a single letter)
- Prevents guessing the same letter twice
- Win/lose detection with clear end-game messages

## How to Play

1. Run the script:
```bash
   python hangman_game.py
```
2. When prompted, type a single letter and press Enter.
3. Keep guessing until you reveal the full word or run out of attempts (6 total).

## Concepts Used

- Variables and data types
- Lists and list operations (`.append()`, `in`)
- `for` loops and `while` loops
- `if` / `elif` / `else` conditionals
- Functions and input validation
- The `random` module

## Example Gameplay
========================================
Welcome to Hangman!
Guess the secret word one letter at a time.
You have 6 attempts.
Word: *******
Remaining attempts: 6
Guess a letter: p
Correct!
Word: P******
...
You WIN! The word was: PROGRAM

## Author

Kate Aubrey Gozum