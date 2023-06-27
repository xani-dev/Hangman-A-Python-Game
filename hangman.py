from random_word import RandomWords

from colorama import Fore, Style

# def hangman_game():

# Hangman pics
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Pick a random word
r = RandomWords()
word = r.get_random_word()
print(word)

# Welcome
print('Guess the word: '+'_ '*len(word))


# Get a guess form user, a single character
guess = ''
incorrect_guesses = 0
max_incorrect_guessess = 6

while True:
    letters_guessed = [ ]
    guess = input("Enter a letter: ")
    if guess in word and len(guess) == 1 and max_incorrect_guessess != 0:
        print(f'Your guess was: {guess}')
        print('Good guess!')
        appears = word.count(guess)
        print('Letter is in word', appears, 'times')
        letters_guessed.append(letters_guessed)
        letters_guessed = ','.join(guess * appears)
        print(letters_guessed)
        remaining_letters = len(word) - len(letters_guessed)
        print('remaining letters', remaining_letters)
          
            
    elif guess not in word and len(guess) == 1 and max_incorrect_guessess != 0:
        print(Fore.RED + 'Oops! That letter is not in the word')
        print(HANGMANPICS[incorrect_guesses])
        print(Style.RESET_ALL)   
        incorrect_guesses += 1
        max_incorrect_guessess -= 1
        print("Guesses left: ", max_incorrect_guessess)
    else:
        print("You have no more guesses available. GAME OVER!")
        print(Fore.CYAN + f'The word was: {word}')
        print(Style.RESET_ALL)  
        break
        
    #TODO:
    # show alert when letter has been chosen before, don't count towards counter
    # limit nums of chars in guess - print("Please enter a single character to continue\n")
    # show the player their current progress in the UI "lines"



