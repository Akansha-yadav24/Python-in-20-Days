import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer', "coders","Coding","learning"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(f"\nWord to guess: {display_word(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print("Incorrect guess.")
        
        if set(word) == guessed_letters:
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

hangman()
