# A General A* Function and its Application to Slide Puzzles
# CS 470/670 at UMass Boston

import numpy as np

example_1_start = np.array([[2, 8, 3],
                           [1, 6, 4],
                           [7, 0, 5]])

example_1_goal = np.array([[1, 2, 3],
                           [8, 0, 4],
                           [7, 6, 5]])

example_2_start = np.array([[ 2,  6,  4,  8],
                            [ 5, 11,  3, 12],
                            [ 7,  0,  1, 15],
                            [10,  9, 13, 14]])

example_2_goal = np.array([[ 1,  2,  3,  4],
                           [ 5,  6,  7,  8],
                           [ 9, 10, 11, 12],
                           [13, 14, 15,  0]])

# For a given current state, move, and goal, compute the new state and its h'-score and return them as a pair. 
def make_node(state, row_from, col_from, row_to, col_to, goal):
    # Create the new state that results from playing the current move. 
    (height, width) = state.shape
    new_state = np.copy(state)
    new_state[row_to, col_to] = new_state[row_from, col_from]
    new_state[row_from, col_from] = 0
    
    # Count the mismatched numbers and use this value as the h'-score (estimated number of moves needed to reach the goal).
    mismatch_count = 0
    for i in range(height):
        for j in range(width):
            if new_state[i ,j] > 0 and new_state[i, j] != goal[i, j]:
                mismatch_count += 1
   
    return (new_state, mismatch_count)

# For given current state and goal state, create all states that can be reached from the current state
# (i.e., expand the current node in the search tree) and return a list that contains a pair (state, h'-score)
# for each of these states.   
def slide_expand(state, goal):
    node_list = []
    (height, width) = state.shape
    (empty_row, empty_col) = np.argwhere(state == 0)[0]     # Find the position of the empty tile
    
    # Based on the positin of the empty tile, find all possible moves and add a pair (new_state, h'-score)
    # for each of them.
    if empty_row > 0:
        node_list.append(make_node(state, empty_row - 1, empty_col, empty_row, empty_col, goal))
    if empty_row < height - 1:
        node_list.append(make_node(state, empty_row + 1, empty_col, empty_row, empty_col, goal))
    if empty_col > 0:
        node_list.append(make_node(state, empty_row, empty_col - 1, empty_row, empty_col, goal))
    if empty_col < width - 1:
        node_list.append(make_node(state, empty_row, empty_col + 1, empty_row, empty_col, goal))
    
    return node_list
  
# TO DO: Return either the solution as a list of states from start to goal or [] if there is no solution.               
def a_star(start, goal, expand):
    (height, width) = start.shape
    #calculate h'-score of start state
    mismatch_count = 0
    for i in range(height):
        for j in range(width):
            if start[i ,j] > 0 and start[i, j] != goal[i, j]:
                mismatch_count += 1
    #save start state and its h'-score into good_state_pair
    good_state_pair = (start, mismatch_count)
    #save start state array into good_state
    good_state = [good_state_pair[0]]
    #compare start state and goal
    compare_array = np.array_equal(good_state_pair[0], goal)
    #check whether reach the goal state
    while not compare_array:
        #create all states that can be reached from the current state and return state and h'-score
        node_list = slide_expand(good_state_pair[0], goal) 
        #check new states and delete same states as ancestors to avoid a search cycle
        node_list_del = []
        for i in range(len(node_list)):
            for j in range(len(good_state)):
                if np.array_equal(node_list[i][0],good_state[j]):
                    node_list_del.append(i)
        for i in node_list_del:
            del node_list[i] 
        # if node_list is empty, which means all the new states are same as ancestors, then stop searching and return empty list
        if len(node_list) == 0:
            return []
        # good_state_pair = node_list[0]
        # for i in range(len(node_list)): 
        #     if node_list[i][1] < good_state_pair[1]: 
        #         good_state_pair = node_list[i]
        #     elif node_list[i][1] == good_state_pair[1]:
        #         node_list1 = slide_expand(node_list[i][0], goal) 
        #         node_list2 = slide_expand(good_state_pair[0], goal)         
        
        #sort h'-score of the list of open nodes
        for i in range(0, len(node_list)):           
            for j in range(0, len(node_list)-i-1):  
                if (node_list[j][1] > node_list[j + 1][1]):  
                    a = node_list[j]  
                    node_list[j]= node_list[j + 1]  
                    node_list[j + 1]= a         
        # choose the smallest h'-score for next round
        good_state_pair = node_list[0]
        compare_array = np.array_equal(good_state_pair[0], goal)
        # add the current good state into good_state
        good_state.append(good_state_pair[0])
    return good_state

# Find and print a solution for a given slide puzzle, i.e., the states we need to go through 
# in order to get from the start state to the goal state.
def slide_solver(start, goal):
    solution = a_star(start, goal, slide_expand)
    if not solution:
        print('This puzzle has no solution. Please stop trying to fool me.')
        return
        
    (height, width) = start.shape
    if height * width >= 10:            # If numbers can have two digits, more space is needed for printing
        digits = 2
    else:
        digits = 1
    horizLine = ('+' + '-' * (digits + 2)) * width + '+'
    for step in range(len(solution)):
        state = solution[step]
        for row in range(height):
            print(horizLine)
            for col in range(width):
                print('| %*d'%(digits, state[row, col]), end=' ')
            print('|')
        print(horizLine)
        if step < len(solution) - 1:
            space = ' ' * (width * (digits + 3) // 2)
            print(space + '|')
            print(space + 'V')

slide_solver(example_1_start, example_1_goal)       # Find solution to example_1
