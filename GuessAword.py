user_input = ("Welcome to Guess a Word!")
print(user_input)
user_input2 = (" The word has 6 letters _ _ _ _ _ _")
print(user_input2)
guess = input("Start entering letters to try and guess the word. Guess: ").lower()
word = "pretty"
guesses = []

if len(guess) != 1 or not guess.isalpha():
    print("Invalid input, please enter a letter.")
    continue

guesses.append(guess)

actual_word = ""

if guess in word:
    print("Correct!")
else:
    print("Wrong!")

for letter in word:
    if letter in guesses:
        actual_word += letter + " "
    else:
        actual_word += "_ "
    
    print("Word:", actual_word)

if all(letter in guesses for letter in word):
    print("Good job! You guessed the correct word.")

if guess == word:
    print(f"You finished! the word was pretty")
    break
