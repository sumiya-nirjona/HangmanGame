
import random

words = ["python", "computer", "student", "program", "keyboard"]

secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=== Welcome to Hangman Game ===")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

while wrong_guesses < max_wrong_guesses:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Incorrect guesses:", wrong_guesses, "/", max_wrong_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

else:
    print("Game Over!")
    print("The correct word was:", secret_word)
