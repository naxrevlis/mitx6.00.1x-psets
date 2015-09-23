# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
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
    wordOk = False
    for i in secretWord:
        if i in lettersGuessed:
            wordOk = True
        else:
            wordOk = False
            break
    return wordOk


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    wordOk = False
    outputString = ''
    for i in secretWord:
        if i in lettersGuessed:
            outputString += i
        else:
            outputString += '_'
    return outputString


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availibleLetters = string.ascii_lowercase
    for i in lettersGuessed:
        if i in availibleLetters:
            availibleLetters = availibleLetters.replace(i, '')
    return availibleLetters


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
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    i = 0
    guessedLetters = []
    numberOfGuesses = 8
    while i != numberOfGuesses:
        print '-----------'
        print 'You have ' + str(numberOfGuesses - i) + ' guesses left.'
        print 'Available Letters :' + getAvailableLetters(guessedLetters)
        guess = raw_input('Please guess a letter: ').lower()
        if guess in guessedLetters:
            print "Oops! You've already guessed that letter:" + getGuessedWord(secretWord, guessedLetters)
        else:
            guessedLetters.append(guess.lower())
            if isWordGuessed(secretWord, guessedLetters):
                print 'Good guess: ' + secretWord
                print '-----------\nCongratulations, you won!'
                break
            elif guess in secretWord:
                print 'Good guess: ' + getGuessedWord(secretWord, guessedLetters)
            else:
                print 'Oops! That letter is not in my word:' + getGuessedWord(secretWord, guessedLetters)
                i += 1
    if i == numberOfGuesses:
        print '-----------\nSorry, you ran out of guesses. The word was else. '


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'test'
#secretWord = chooseWord(wordlist).lower()

print hangman(secretWord)
