import random

words = ["test", "play", "hangman", "tractor"]
word = words[random.randrange(0,3)]
word_state = []
wrong_guesses = []

gallows1 = "   /----\\=========\n"
gallows2 = "   |    |        |\n"
gallows3 = "   |    |  \n"
gallows4 = "___|    |___\n"
gallows5 = "/ /      \\ \\"
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
    print(currentState)
    
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
    
def makeGuess():
    x = 0 
    rightGuess = False    
    print("Guess a letter: ")
    guess = input()               
    for letter in word:
        x += 1
        if letter == guess:            
            word_state[x-1] = guess 
            rightGuess = True 
    if rightGuess:
        print_word_state()
        return
    else:
        wrong_guesses.append(guess)
        print("Incorrect Letters: ", wrong_guesses)
        print_hangman()
        print_word_state()

print_word_state()
while len(wrong_guesses) < 10:
    makeGuess()
