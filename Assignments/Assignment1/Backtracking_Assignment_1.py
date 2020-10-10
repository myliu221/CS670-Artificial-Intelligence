# An Even More General Backtracking Function and its Application to the n-Queens Problem
# Assignment #1 for CS 470/670 at UMass Boston

import copy
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


# "Sanity check" function for the n-queens problem.
# For a given search state (node), it checks whether the next decision could possibly lead to a solution 
def queens_check(current_state, decision_info, next_option):
    for column in range(decision_info):
        row_distance = abs(current_state[column] - next_option)
        if row_distance == 0 or row_distance == decision_info - column:
            return (False, None)
    new_state = copy.deepcopy(current_state)
    new_state[decision_info] = next_option
    return (True, new_state)

# Recursive backtracking function that receives the options for the problem's sequence of decisions,
# a reference to a "sanity check" function and, optionally, the current search path.
# It returns the result as a pair (success indicator, list of n row indices for queen placement).
def backtrack(decision_seq, check_func, current_state, depth=0):
    for next_option in decision_seq[depth][1]:
        (success, new_state) = check_func(current_state, decision_seq[depth][0], next_option)
        print('  ' * depth + 'Check state ' + str(current_state) + ' with next option ' + str(next_option) + '-> ' + str(success))
        if success and depth < len(decision_seq) - 1:
            (success, new_state) = backtrack(decision_seq, check_func, new_state, depth + 1)
        if success:
            return (True, new_state)
    return (False, None)

# Finds a solution for the n-queens problem, i.e., a pair (success indicator, list of n row indices for queen placement)
def n_queens_solver(n):
    initial_state = [0 for i in range(n)]
    decision_seq = [(i, list(range(1, n + 1))) for i in range(n)]
    return backtrack(decision_seq, queens_check, initial_state)

# Solves the n-queens problem and prints the solution in ASCII format 
def n_queens_ascii(n):
    (success, solution) = n_queens_solver(n)
    if not success:
        print('Sorry, there is no solution to the %d-queens problem.'%(n))
    else:
        print('Solution: ' + str(solution))
        for y in range(1, n + 1):
            for x in range(0, n):
                if solution[x] == y:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print('')

n_queens_ascii(4)