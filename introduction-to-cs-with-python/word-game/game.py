# The 6.00 Word Game
'''
This game is a lot like Scrabble or Words With Friends.
Letters are dealt to players, who then construct one or more words out of their letters. 
Each valid word receives a score, based on the length of the word and the letters in that word.

The rules of the game are as follows:

Dealing:
    - A player is dealt a hand of n letters chosen at random (assume n=7 for now).
    - The player arranges the hand into as many words as they want out of the letters, using each letter at most once.
    - Some letters may remain unused (these won't be scored).

Scoring:
    - The score for the hand is the sum of the scores for each word formed.
    - The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.
    - Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.
    - For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!
    - As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).
'''

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word, write a function
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # initialize score
    score = 0

    # if word is an empty string return score which is 0 at this point
    if word == "":
        return score

    else:
        # case when the player uses all the letters in his hand and is given extra points
        if len(word) == n:
            # for every letter in the word get the value associated with this letter's key in the SCRABBLE_LETTER_VALUES dict
            # then increment the score by this value
            for letter in word:
                value = SCRABBLE_LETTER_VALUES.get(letter)
                score += value

            # multiply the value of all the letters by the word's length to get the final score
            score *= len(word)
            # add a bonus of 50 points for using all the letters
            score += 50
            return score
        # case when the player does not use all the letters in his hand
        else:
            for letter in word:
                value = SCRABBLE_LETTER_VALUES.get(letter)
                score += value

            score *= len(word)
            return score


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters, write a function
#


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # create a shallow copy of the hand in order not to mutate the original hand
    updatedHand = hand.copy()

    # for every letter in the word decrease the value of this letter's key by one
    for letter in word:
        updatedHand[letter] = updatedHand.get(letter) - 1

    return updatedHand


#
# Problem #3: Test word validity, write a function
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # Store a list of the letters that appears in word without any duplicates
    listOfWordLetters = list(word)
    setOfWordLetters = set(listOfWordLetters)
    wordLettersNoDuplicates = list(setOfWordLetters)

    # Check if the word is in the wordlist
    if word in wordList:
        for letter in wordLettersNoDuplicates:
            # for every unique letter that appears in the word count how many times it appears
            numberOfAppearancesInWord = word.count(letter)
            # if the letter is not in players hand return false
            if letter not in hand.keys():
                return False
            # check if player's hand has sufficient number of a given letter, if not return False
            else:
                if hand[letter] >= numberOfAppearancesInWord:
                    continue
                else:
                    return False
    # If the word is not in the wordlist, return false
    else:
        return False

    return True

#
# Problem #4: Playing a hand, write functions
#


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    handsLength = 0

    for letter in hand.keys():
        handsLength += hand.get(letter)

    return handsLength


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # Keep track of the total score
    playerScore = 0

    while calculateHandlen(hand) > 0:
        # Display the hand
        print("Current Hand: ", end="")
        displayHand(hand)

        # Ask user for input
        usersWord = input(
            'Enter word, or a "." to indicate that you are finished: ')

        # If the input is a single period:
        if usersWord == '.':
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:

            # If the word is not valid:
            if isValidWord(usersWord, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print()
                continue

            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                scoreForWord = getWordScore(usersWord, n)
                playerScore += scoreForWord
                print("\"" + usersWord + "\"", "earned", scoreForWord,
                      "points. Total:", playerScore, "points")
                print()

                # Update the hand TODO: nie działa, nie updateuje handa,
                hand = updateHand(hand, usersWord)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) == 0:
        print("Run out of letters. Total score:", playerScore, "points.")
    else:
        print("Goodbye! Total score: ", playerScore, "points.")
        print()

#
# Problem #5: Playing a game, write a function
#


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1    
    """
    # initilize the current hand
    playedHands = 0
    currentHand = {}

    while True:
        userChoice = input(
            "Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        # If the user chooses to be dealt a new hand, replace the current hand with a random generated one
        # and pass it to the playHand function to let the user play this hand
        if userChoice == "n":
            currentHand = dealHand(HAND_SIZE)
            playHand(currentHand, wordList, HAND_SIZE)
            playedHands += 1
        # If the user chooses to play with the same hand again, do not call the dealHand function,
        # the currentHand stays the same
        elif userChoice == "r" and playedHands != 0:
            playHand(currentHand, wordList, HAND_SIZE)
            playedHands += 1
        # If the user chooses to play with the same hand again, but have not played any hand before
        elif userChoice == "r" and playedHands == 0:
            print("You have not played a hand yet. Please play a new hand first!")
            print()
            continue
        elif userChoice == "e":
            break
        else:
            print("Invalid command.")
            continue


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
