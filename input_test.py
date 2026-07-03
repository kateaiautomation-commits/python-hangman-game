while True:
    guess = input("Enter a letter: ")
    
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter exactly one letter.")
        continue
    else:
        print("You entered:", guess)
        break