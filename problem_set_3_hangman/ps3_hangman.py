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
    # FILL IN YOUR CODE HERE...
    foundAllLetters = True
    for letter in range(len(secretWord)):
        if secretWord[letter] not in lettersGuessed:
            foundAllLetters = False
            break
    return foundAllLetters

#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#secretWord = 'aei'
#print isWordGuessed(secretWord, lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    blanks = '_ ' * len(secretWord)
    for letter in range(len(secretWord)):
        if secretWord[letter] in lettersGuessed:
            blanks = blanks[:(2 * letter)] + secretWord[letter] + blanks[2 * (letter) + 1:]
    return blanks
    """
    for letter in range(len(secretWord)):
        if secretWord[letter] not in lettersGuessed:
            secretWord = secretWord[:letter] + "_"  + secretWord[letter+1:]
    return secretWord
    """


#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#secretWord = 'bbbebbebieii'
#print getGuessedWord(secretWord, lettersGuessed)




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabet = string.ascii_lowercase
    AvailableLetters = ''
    for letter in range(len( alphabet)):
        if  alphabet[letter] not in lettersGuessed:
            AvailableLetters +=alphabet[letter]
    return AvailableLetters


#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print getAvailableLetters(lettersGuessed)


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
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game, Hangman! "
    print "I am thinking of a word that is %d letters long." %(len(secretWord))
    lettersGuessed = []
    num_Guesses = 8
    while num_Guesses>0:
        print "-------------"
        print "You have %d guesses left."%(num_Guesses)
        print "Available letters: %s" % (getAvailableLetters(lettersGuessed))
        new_letter = raw_input("Please guess a letter: ")
        new_letter = new_letter.lower()
        if new_letter not in lettersGuessed:
            lettersGuessed.append(new_letter)
            if new_letter in secretWord:
                print "Good guess: %s" % (getGuessedWord(secretWord, lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    print "-------------"
                    print "Congratulations, you won!"
                    break
            else:
                print "Oops! That letter is not in my word: %s" % (getGuessedWord(secretWord, lettersGuessed))
                num_Guesses -= 1
        else:
            print "Oops! You've already guessed that letter: %s" % (getGuessedWord(secretWord, lettersGuessed))
    print "-------------"
    if num_Guesses==0:
        print "Sorry, you ran out of guesses. The word was %s ."% (secretWord)
    return


    # When you've completed your hangman function, uncomment these two lines
    # and run this file to test! (hint: you might want to pick your own
    # secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
#secretWord = 'guanabana'
hangman(secretWord)
