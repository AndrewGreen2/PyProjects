import random

words = ["test", "play", "hangman", "tractor"]
word = words[random.randrange(0,3)]
word_state = []
wrong_guesses = []
print(word)

for i in range(len(word)):
    word_state.append("_")

def print_word_state():
    currentState = ""
    for i in word_state:
        currentState = currentState + i
    print(currentState)

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
    else:
        wrong_guesses.append(guess)
        print("Incorrect Letters: ", wrong_guesses)
        print_word_state()

print_word_state()
while len(wrong_guesses) < 6:
    makeGuess()
