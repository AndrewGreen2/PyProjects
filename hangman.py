import random

with open("words.txt", "r") as f:
    words = f.read().splitlines()
f.close

word = words[random.randrange(0,len(words))].lower()
word_state = []
wrong_guesses = []

gallows1 = "   /----\\=========>\n"
gallows2 = "   |    |        |\n"
gallows3 = "   |    |  \n"
gallows4 = "___|    |___\n"
gallows5 = "/ /      \\ \\___________"
head = "   (o _ o)  \n"
deadhead = "   (x _ x)  \n"
body = " /(       )\\ \n"
legs = "  _/   \\_\n"

for i in range(len(word)):
    word_state.append("_")

def print_word_state():
    currentState = ""
    for i in word_state:
        currentState = currentState + i
    return(currentState.capitalize())
    
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
        exit()
    print(hangman)

def validGuess(guess):
    if guess.isalpha() == False:
        print("Please guess a letter or word.")
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
    if validGuess(guess):
        if len(guess) > 1:   
            if guess == word:
                print("Congratulations! The correct word was: " + word.capitalize())
                exit()       
        for letter in word:
            x += 1
            if letter.lower() == guess:            
                word_state[x-1] = guess 
                rightGuess = True
        if rightGuess:
            if print_word_state().lower() == word:
                print("Congratulations! The correct word was: " + word.capitalize())
                exit()     
            print('\n' + print_word_state())
            return
    wrongGuess(guess)

def wrongGuess(guess):
    wrong_guesses.append(guess)
    print("\n" + "Sorry, that guess was incorrect!" + "\n" + "Incorrect guesses: ", wrong_guesses, "\n")
    print_hangman()
    print('\n' + print_word_state())

if __name__ == "__main__":
    print("Let's play Hangman! Good luck.\n\n")
    print(print_word_state())
    while len(wrong_guesses) < 10:
        makeGuess()
