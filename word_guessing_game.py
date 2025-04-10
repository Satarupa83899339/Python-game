import random
import re

# Function to read words from a file
def read_words():
    try:
        with open('words.txt', 'r') as file:
            words = file.read().splitlines()
            return [word.lower() for word in words if word]  # Filter out empty lines
    except FileNotFoundError:
        print('❌ words.txt does not exist. Please add the file with some words.')
        return []

# Function to display current state of the word
def display_word(secret_word, guessed_letters):
    word_to_display = ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])
    print(f"\nWord: {word_to_display}")

# Function to get a valid guess from the user
def get_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("⚠️ Enter only one letter.")
        elif not re.match('^[a-z]$', guess):
            print("⚠️ Enter a valid letter from a to z.")
        elif guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
        else:
            return guess

# Function to check if the entire word is guessed
def is_word_guessed(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)

# Main function
def main():
    words = read_words()
    if not words:
        return  # Exit if no words found

    secret_word = random.choice(words)
    attempts = 6
    guessed_letters = []

    print("🎮 Welcome to the Word Guessing Game!")
    print(f"🔠 The word has {len(secret_word)} letters. You have {attempts} attempts.\n")

    while attempts > 0:
        display_word(secret_word, guessed_letters)
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Good guess!")
            if is_word_guessed(secret_word, guessed_letters):
                display_word(secret_word, guessed_letters)
                print("\n🎉 Congratulations! You guessed the word correctly!")
                break
        else:
            attempts -= 1
            print(f"❌ Wrong guess. Attempts left: {attempts}")
            if attempts == 0:
                print(f"\n💀 Game over! The correct word was: {secret_word}")

if __name__ == '__main__':
    main()
