# A General Backtracking Function and its Application to Sudoku Puzzles
# CS 470/670 at UMass Boston

import numpy as np

example_1 = np.array([[1, 0, 8, 5, 3, 0, 7, 0, 0],
                      [2, 0, 6, 0, 0, 8, 0, 3, 0],
                      [0, 0, 0, 0, 0, 4, 2, 5, 8],
                      [0, 0, 0, 0, 0, 5, 8, 1, 0],
                      [4, 2, 0, 0, 0, 0, 0, 6, 3],
                      [0, 8, 3, 2, 0, 0, 0, 0, 0],
                      [3, 6, 2, 4, 0, 0, 0, 0, 0],
                      [0, 7, 0, 6, 0, 0, 3, 0, 9],
                      [0, 0, 4, 0, 7, 3, 6, 0, 5]])

example_2 = np.array([[0, 0, 0, 0, 3, 0, 2, 8, 0],
                      [7, 0, 0, 5, 0, 0, 0, 1, 0],
                      [3, 0, 0, 0, 6, 0, 0, 0, 0],
                      [0, 8, 0, 0, 0, 2, 0, 4, 0],
                      [1, 0, 0, 0, 5, 0, 0, 0, 2],
                      [0, 6, 0, 9, 0, 0, 0, 3, 0],
                      [0, 0, 0, 0, 2, 0, 0, 0, 4],
                      [0, 4, 0, 0, 0, 6, 0, 0, 1],
                      [0, 9, 2, 0, 7, 0, 0, 0, 0]])


# "Sanity check" function for the sudoku problem.
# For a given search path, it checks whether the next decision could possibly lead to a solution,
# and if so, returns teh state resulting from the move. 
def sudoku_check(current_state, decision_info, next_option):
    (row, column) = decision_info
    if next_option in current_state[row, :] or next_option in current_state[:, column]:
        return (False, None)
    (block_top, block_left) = (3 * int(row / 3), 3 * int(column / 3))
    if next_option in current_state[block_top:block_top + 3, block_left:block_left + 3]:
        return (False, None)
    new_state = np.copy(current_state)
    new_state[decision_info] = next_option
    return (True, new_state)
    
# Recursive backtracking function that receives the options for the problem's sequence of decisions,
# a reference to a "sanity check" function and, optionally, the current search path.
# It returns a solution of the problem or None if there is no solution.
def backtrack(decision_seq, check_func, current_state, depth=0):
    for next_option in decision_seq[depth][1]:
        (success, new_state) = check_func(current_state, decision_seq[depth][0], next_option)
        if success and depth < len(decision_seq) - 1:
            (success, new_state) = backtrack(decision_seq, check_func, new_state, depth + 1)
        if success:
            return (True, new_state)
    return (False, None)

# Finds a solution, i.e., a list of decisions, for a given Sudoku puzzle
def sudoku_solver(puzzle):
    decision_seq = []
    for row in range(9):
        for column in range(9):
            if puzzle[row, column] == 0:
                valid_options = []
                for option in range(1, 10):
                    (success, _) = sudoku_check(puzzle, (row, column), option)
                    if success:
                        valid_options.append(option)
                if valid_options == []:
                    print('Sorry, this puzzle has no solution.')
                    return
                if len(valid_options) == 1:
                    puzzle[row, column] = valid_options[0]
                else:
                    decision_seq.append(((row, column), valid_options)) 
    (success, solution) = backtrack(decision_seq, sudoku_check, puzzle)
    if not success:
        print('Sorry, this puzzle has no solution.')
        return
    print(solution)
    
sudoku_solver(example_1)
