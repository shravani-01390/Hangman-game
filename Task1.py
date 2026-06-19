import random

# List of predefined words
words = ["python", "apple", "school", "computer", "banana"]

# Select a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")

while incorrect_guesses < max_guesses and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    if guess in word:
        print("Correct!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# Check win or lose
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)