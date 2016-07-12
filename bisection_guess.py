print "Please think of a number between 0 and 100!: "
lo = 0
hi = 100
guessed = False
while not guessed:
    guess = (hi + lo) / 2
    print 'Is your secret number ' + str(guess) + '?'
    respond = raw_input(" Enter 'h' to indicate the guess is too high." \
                        " Enter 'l' to indicate the guess is too low."  \
                        " Enter 'c' to indicate I guessed correctly. ")
    if respond == 'c':
       guessed = True  # Guessed correctly!
    elif respond == 'h':
        hi = guess     # Guess too high. let current guess be highest possible guess.
    elif respond == 'l':
        lo = guess     # Guess too low. let current guess be lowest possible guess.
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))

