secret_word = "cat"
guessed_letters = ["a"]

hidden_secret_word = ""
for letter in secret_word:
    if letter in guessed_letters:
        hidden_secret_word += letter
    else:
        hidden_secret_word += "*"

print(hidden_secret_word)