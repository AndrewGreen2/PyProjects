import pyautogui as pg
import time


board = []

while True:
    row = list(input('Row: '))
    ints = []
    
    for n in row:
        ints.append(int(n))
    board.append(ints)
    
    if len(board) == 9:
        break
    print('Row ' + str(len(board)) + ' Complete ')
    
time.sleep(2)

def input_answer(solution):
    final = []
    for lists in solution:
        for num in lists:
            final.append(str(num))
    
    counter = []

    for num in final:
        pg.press(num) #pyautogui function for pressing number on keyboard
        pg.hotkey("right") # press number and key to the right
        counter.append(num)
        if len(counter) % 9 == 0: # start new line
            pg.hotkey("down")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")
            pg.hotkey("left")

def find_empty_space(puzzle):
    # finds the next row, col on the puzzle which isn't filled
    # returns row, col tuple (None,None) if no empty space exists
    
    for r in range(9):
        for c in range(9):  # range(9) is 0,1,2,3, ... 8
            if puzzle[r][c] == 0:
                return r, c
            
    return None, None
   
def is_valid(puzzle, guess, row, col):
    # check whether the guess at row/col is valid (True), else return False
    
    # check row for duplicate nums
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # check col for duplicate nums
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # check 3x3 grid for duplicates
    # defining start of rows & columns so we can iterate over them    
    row_start = (row // 3) * 3  # 1 // 3 = 0, 5 // 3 = 1, ...
    col_start = (col // 3) * 3
     
    # checking if our guess exists in any of the 3x3 grids - if so, return false   
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    return True
    
         
    

def sudoku_solver(puzzle):
    # function to solve a sudoku puzzle using backtracking
    # puzzle input will be a list of lists, where each inner list is a row in the sudoku puzzle
    # mutates the list to be the solution (if it exists) 

    row, col = find_empty_space(puzzle)
    
    
    # 1: if there are no empty spaces, puzzle is solved
    if row is None:
        return True
    
    
    # # 2: if there is an empty space, guess a number 1-9
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess 
            if sudoku_solver(puzzle):
                return True
    
    # # 4: if guess is invalid or does not solve puzzle, backtrack and try again
        puzzle[row][col] = 0
    
    # # 5: if no numbers work - puzzle is unsolvable
    return False

if __name__ == '__main__':
    # board = [
    #     [9, 0, 0,   0, 8, 0,   0, 0, 0],
    #     [0, 6, 0,   1, 0, 0,   7, 3, 0],
    #     [0, 0, 0,   0, 0, 0,   0, 0, 4],

    #     [0, 0, 0,   4, 0, 0,   0, 0, 6],
    #     [0, 0, 8,   0, 1, 0,   5, 4, 0],
    #     [0, 5, 0,   0, 0, 0,   0, 0, 2],

    #     [0, 7, 0,   3, 0, 0,   1, 5, 0],
    #     [0, 0, 6,   0, 0, 7,   0, 0, 0],
    #     [0, 0, 0,   0, 0, 0,   2, 0, 0]        
    # ]
    print(sudoku_solver(board))
    print(board)
    input_answer(board)
    print('done.')
