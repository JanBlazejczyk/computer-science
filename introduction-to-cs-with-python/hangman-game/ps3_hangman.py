# Hangman game
#

# -----------------------------------
# Helper code already there for the exercise

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code, beggining of my own code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # set up the initial index value to increment
    secretWordIndex = 0
    # iterate throught the letters in the correct word that needs to be guessed by the player
    for letter in secretWord:
        # if the letter of the correct word is in the list of the letters the player has already guessed
        # and we did not reach the last letter of the correct word
        # we increment the index and move to the next iteration
        if letter in lettersGuessed and secretWordIndex != len(secretWord) - 1:
            secretWordIndex += 1
            continue
        # if we reached the last letter of the correct word and it is in the guessed letter list, return true
        elif letter in lettersGuessed and secretWordIndex == len(secretWord) - 1:
            return True
        # if any of the letters of the correct word is not on the user guessed list, the user did not guessed the word yet and return false
        else:
            return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # initialize an empty string with a word to be display
    wordToDisplay = ''

    # iterate through every letter of the correct word the user needs to guess
    for letter in secretWord:
        # if the letter is in users guessed list, we display the letter on the given spot by adding it to the string
        if letter in lettersGuessed:
            wordToDisplay += (letter + " ")
        # if the letter is not in users guessed list, we display an underscore on the given spot by adding it to the string
        else:
            wordToDisplay += "_ "

    return wordToDisplay


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # this is a variable that holds all the letters of the alphabet
    allLetters = string.ascii_lowercase

    # create a string of every letter that is not on the user guessed list
    availableLetters = ''.join([allLetters[i] for i in range(
        len(allLetters)) if allLetters[i] not in lettersGuessed])

    return availableLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Print the welcome message and the information how many letters does the word to be guessed contains
    print('Welcome to the game of Hangman!')
    secretWordlength = len(secretWord)
    print('I am thinking of a word that is', secretWordlength, 'letters long.')

    # initialize the list of the letters that the user has already guessed
    lettersGuessed = []

    # initialize number of guesses that the user has
    guesses = 8

    # loop until the number of guesses reaches 0, which means that the game is over
    while guesses > 0:
        print('------------')
        # display number of guesses left and the list of the letters that are yet to be guessed
        print('You have', guesses, 'guesses left.')
        print("Available letters:", getAvailableLetters(lettersGuessed))

        # ask the user for his next guess and convert it to lowercase
        playerGuess = input('Please guess a letter: ')
        playerGuessLower = playerGuess.lower()

        # user guessed correctly and he typed in the letter for the first time
        # add the letter to the list of the letters already guessed
        # do not decrement the number of guesses, because this was a correct guess
        if playerGuessLower in secretWord and playerGuessLower not in lettersGuessed:
            lettersGuessed.append(playerGuessLower)
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))

        # user guessed correctly but the letter was already typed in before
        # do not decrement the number of guesses, because this guess has been already made
        elif playerGuessLower in secretWord and playerGuessLower in lettersGuessed:
            print("Oops! You've already guessed that letter:",
                  getGuessedWord(secretWord, lettersGuessed))

        # user guessed incorrectly and he typed in the letter for the first time
        # add the letter to the list of the letters already guessed
        # decrement the number of guesses, because this was a wrong guess
        elif playerGuessLower not in secretWord and playerGuessLower not in lettersGuessed:
            lettersGuessed.append(playerGuessLower)
            print('Oops! That letter is not in my word:',
                  getGuessedWord(secretWord, lettersGuessed))
            guesses -= 1

        # user guessed incorrectly but the letter was already typed in before
        # do not decrement the number of guesses, because this guess has been already made
        elif playerGuessLower not in secretWord and playerGuessLower in lettersGuessed:
            print("Oops! You've already guessed that letter:",
                  getGuessedWord(secretWord, lettersGuessed))

        # this block of code checks if the user has already guessed the whole word correctly using the isWordGuessed() function
        # if the isWordGuessed() function is true (the user has all the needed letters) and the user still have guesses left
        # the user won and the loop breakes
        if isWordGuessed(secretWord, lettersGuessed) == True and guesses > 0:
            print('------------')
            print('Congratulations, you won!')
            break

        # if the isWordGuessed() function is false (the user does not have all the needed letters) but the user still have guesses left
        # we continue with another execution of the loop
        elif isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
            continue

        # if the number of guesses reaches 0
        # the user lost and the secret word is revealed
        else:
            print('------------')
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
