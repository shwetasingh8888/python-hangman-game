import random

# List of 5 predefined words
words = ["india ", "hello", "newyear", "rose", "learn"]

# Randomly choose a word from the list
word_to_guess = random.choice(words)
guessed_letters = []  # Store letters the player has guessed
incorrect_guesses = 0
max_incorrect = 6

# Create the display version of the word with underscores
display_word = ["_" for _ in word_to_guess]

print("Welcome to Hangman!")
print("You have 6 incorrect guesses allowed.")
print(" ".join(display_word))

# Game loop
while incorrect_guesses < max_incorrect and "_" in display_word:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        # Reveal all positions of the guessed letter
        for idx, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[idx] = guess
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print(f"Incorrect guess! You have {max_incorrect - incorrect_guesses} tries left.")

    print(" ".join(display_word))

# End of game
if "_" not in display_word:
    print(f"Congratulations! You guessed the word: {word_to_guess}")
else:
    print(f"Game Over! The word was: {word_to_guess}")
