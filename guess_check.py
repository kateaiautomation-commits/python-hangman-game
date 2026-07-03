secret_word = "cat"
correct_letters = []
wrong_letters = []
remaining_attempts = 6

input_letter = input("Guess a letter: ")

if input_letter in secret_word:
    correct_letters.append(input_letter)
    print("Correct! You guessed:", input_letter)
else:
    wrong_letters.append(input_letter)
    remaining_attempts -= 1
    print("Wrong guess. Remaining attempts:", remaining_attempts)

print("Correct letters so far:", correct_letters)
print("Wrong letters so far:", wrong_letters)