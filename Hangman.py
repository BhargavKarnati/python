import string
import random


def hangman(secret_word):
    # Set of vowels
    vowels = set('aeiou')

    # Initialize variables
    guesses_remaining = 6
    letters_guessed = set()
    unique_letters = set(secret_word)
    
    print(f"Welcome to Hangman!")
    print(f"The secret word contains {len(secret_word)} letters.")
    print(f"You start with {guesses_remaining} guesses.\n")
    
    def get_guessed_word(secret_word, letters_guessed):
        # Return the word with correct guesses and underscores for remaining letters
        return ''.join([letter if letter in letters_guessed else '_ ' for letter in secret_word])

    def get_available_letters(letters_guessed):
        # Return the letters that have not been guessed yet
        return ''.join([letter for letter in string.ascii_lowercase if letter not in letters_guessed])
    
    while guesses_remaining > 0:
        # Show current state of the game
        print(f"Guesses remaining: {guesses_remaining}")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        # Get a guess from the user
        guess = input("Please guess a letter: ").lower()
        
        # Ensure valid input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.\n")
            continue
        
        if guess in letters_guessed:
            print(f"Oops! You've already guessed that letter: {get_guessed_word(secret_word, letters_guessed)}\n")
            continue

        letters_guessed.add(guess)

        if guess in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}\n")
            if all(letter in letters_guessed for letter in secret_word):
                # User wins
                score = guesses_remaining * len(unique_letters)
                print(f"Congratulations! You've guessed the word '{secret_word}' and won the game!")
                print(f"Your total score is: {score}\n")
                return
        else:
            if guess in vowels:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print(f"Oops! That letter is not in the word: {get_guessed_word(secret_word, letters_guessed)}\n")

    # Game over - user loses
    print(f"Sorry, you ran out of guesses. The word was '{secret_word}'. Better luck next time!\n")





words = ['army', 'beautiful', 'became', 'if', 'actually', 'beside', 
         'between','come','eye','five','fur','imposter', 'problem' ,
         'revenge' ,'few' ,'circle' ,'district','trade','quota','stop','depressed','disorder','dentist']


random_word = random.choice(words)

#check you function
hangman(random_word)