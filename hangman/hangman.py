import random


with open("words.txt", "r") as f:
    words = f.read().splitlines()
f.close
    
#----------------------------------------------------------

gallows1 = "   /----\\=========>\n"
gallows2 = "   |    |        |\n"
gallows3 = "   |    |  \n"
gallows4 = "___|    |___\n"
gallows5 = "/ /      \\ \\___________"
head = "   (o _ o)  \n"
deadhead = "   (x _ x)  \n"
body = " /(       )\\ \n"
legs = "  _/   \\_\n"

#----------------------------------------------------------


def initiate():
    print("Let's play Hangman! Good luck.\n\n")
    global word
    global word_state
    global wrong_guesses
    word = words[random.randrange(0,len(words))].lower()
    word_state = []
    wrong_guesses = []
    hangman = ""
    for i in range(len(word)):
        word_state.append("_")
    print(print_word_state())

def print_word_state():
    currentState = ""
    for i in word_state:
        currentState = currentState + i
    return(currentState.capitalize())

def play_again():
    answer = input("Would you like to play again? (Y/N): ").lower().strip()    
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input Y or N.")
        answer = input("Would you like to play again? (Y/N): ").lower().strip()        
    if answer[0] == "y":
        initiate()
    else:
        exit()

    
def print_hangman(): 
    hangman = "" 
    if len(wrong_guesses)>0:
        hangman = hangman + gallows4 + gallows5
    if len(wrong_guesses)>1:
        hangman = gallows3 + gallows3 + hangman
    if len(wrong_guesses)>2:
        hangman = gallows3 + gallows3 + hangman
    if len(wrong_guesses)>3:
        hangman = gallows1 + gallows2 + gallows3 + gallows3 + gallows4 + gallows5
    if len(wrong_guesses)>4:
        hangman = gallows1 + gallows2 + gallows3[:-1] + head + gallows3  + gallows4 + gallows5
    if len(wrong_guesses)>5:
        hangman = gallows1 + gallows2 + gallows3[:-1] + head + gallows3[:-1] + body +gallows4 +  gallows5
    if len(wrong_guesses)>6:
        print("Game Over!")
        hangman = gallows1 + gallows2 + gallows3[:-1] + deadhead + gallows3[:-1] + body + gallows4[:-1] + legs + gallows5
        print(hangman)
        play_again()
    print(hangman)

def validGuess(guess):
    if guess.isalpha() == False:
        print("Please guess a letter or word.")
        return False
    for i in word_state:
        if i == guess:
            print("You have already guessed this letter!")
            print('\n' + print_word_state())
            return False
    for i in wrong_guesses:
        if i == guess:
            print("You have already guessed this letter!")
            print('\n' + print_word_state())
            return False
    return True
    
def makeGuess():
    x = 0
    rightGuess = False    
    print("\nGuess a letter or word: ")
    guess = input().lower()
    if validGuess(guess) == True:
        if len(guess) > 1:   
            if guess == word:
                print("Congratulations! The correct word was: " + word.capitalize())
                play_again()       
        for letter in word:
            x += 1
            if letter.lower() == guess:            
                word_state[x-1] = guess 
                rightGuess = True
        if rightGuess:
            if print_word_state().lower() == word:
                print("Congratulations! The correct word was: " + word.capitalize())
                play_again()     
            print('\n' + print_word_state())
            return
        wrongGuess(guess)

def wrongGuess(guess):
    wrong_guesses.append(guess)
    print("\n" + "Sorry, that guess was incorrect!" + "\n" + "Incorrect guesses: ", wrong_guesses, "\n")
    print_hangman()
    print('\n' + print_word_state())

if __name__ == "__main__":
    initiate()
    while len(wrong_guesses) < 10:
        makeGuess()
