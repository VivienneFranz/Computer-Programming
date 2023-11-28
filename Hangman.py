import random


def get_random_word_hangmanlist():
    

    with open('sowpods.txt', 'r') as file:

        wordlist = file.read().split("/n")
        
    secret_word = random.choice(wordlist)
    return word

guesses = []
secret_word = get_random_word_hangmanlist()
attemps = 6

def display_word(secret_word, guesses):

    display = ""
    for letter in secret_word:
        if letter in guesses:

            display += letter
        else:

            display += "_"


print("Welcome to Hangman!")

print(display_word(secret_word, guesses))


while "_" in display_word(secret_word, guesses) and attempts > 0:

    guess = input("Guess a letter:").lower()


if len(guess) != 1 or not guess.isalpha():

    print("Invalid input, please enter a letter.")


guesses.append(guess)

actual_word = ""

if guess in word:

    print("Correct!")
else:

    print("Wrong!")

    attempts -= 1

    print(f"You have {attempts} attempts left")

print()
for letter in word:
    if letter in guesses:

        actual_word += letter + " "
    else:

        actual_word += "_ "
    

    print("Word:", actual_word)


if all(letter in guesses for letter in word):

    print("Good job! You guessed the correct word.")

if guess == word:

    print(f"You finished!")

