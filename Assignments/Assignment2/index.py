#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:36:43 2020

@author: mingyu.liu001
"""
import numpy as np
# initial_state = [1,5,3,4,2,6,7,8,0]
# goal_state = [0,1,2,3,4,5,6,7,8]
# def calculateManhattan(initial_state):
#     initial_config = initial_state
#     manDict = 0
#     for i,item in enumerate(initial_config):
#         prev_row,prev_col = int(i/ 3) , i % 3
#         goal_row,goal_col = int(item /3),item % 3
#         manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
#     return manDict

# calculateManhattan(initial_state)


a = np.array([[2, 8, 3],
              [1, 6, 4],
              [7, 0, 5]])

b = np.array([[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]])


#c=a.tolist()
d=list(a.flatten())

e= d.index(8)

d2=list(b.flatten())

e2= d2.index(8)

cur_i, cur_j = e // int(np.sqrt(len(d))), e % int(np.sqrt(len(d)))
goa_i, goa_j = e2 // int(np.sqrt(len(d2))), e2 % int(np.sqrt(len(d2)))

dis1= abs(cur_i - goa_i) + abs(cur_j- goa_j)


# cur_i, cur_j = e // int(np.sqrt(len(a))), e % int(np.sqrt(len(a)))
# goa_i, goa_j = e2 // int(np.sqrt(len(b))), e2 % int(np.sqrt(len(b)))

# dis2= abs(cur_i - goa_i) + abs(cur_j- goa_j)