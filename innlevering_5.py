# innlevering 5

# Group members:

# Oystein Falkeid
# e-mail: oystein.falkeid@nmbu.no

# Eirik Mentyjaervi
# e-mail: eirik.mentyjarvi@nmbu.no

import sys
from pathlib import Path

#printer til fil i stedenfor terminal
file = Path('.') / Path('terminal.txt')
sys.stdout = open(file, 'w')

print('innlevering 5')
print()

# How to work on this exercise
# This is the last introductory exercise sheet. 
# Starting next week, we will move to the project part of the exercises. 
# Work on exercise 5 together with your partner. 
# Do not share your code with other groups. 
# Use VSCode, virtual environments, and a "requirements.txt" file to install and document packages. 
# Only one person in the group hands in the assignment. 
# If you are the person to submit your solution, send a screenshot of the submission notification 
# to your partner so that both of you know the exercise has been submitted. 
# Indicate both your names and NMBU email addresses on top of your .py file or your notebook. 
# Only share code with your project partner. 
# Persons who hand in alone will not receive points unless we see that they have actively 
# tried to find a partner by adding their name to the Padlet (https://padlet.com/jonaskusch1/exerciseteams2024Links to an external site.) 
# before Tuesday, October 8th.  Use the concepts learned in this course to solve the assignment.

# Upload your solution before Monday at 2 pm as a Python file or Jupyter Notebook. 
# In addition, if you are using a .py file, upload a .txt file with the output of your code. 
# In case you are using a Jupyter Notebook, generate an output pdf and hand it in. 
# Your points will then be uploaded to Canvas. You cannot submit this exercise multiple times. 
# Exercises that give 0 points are meant to help you or provide a deeper understanding. 
# Since they do not give points, you do not have to solve them, but they will help you become a good programmer. 
# Moreover, if you are unfamiliar with matrices, vectors, and simple matrix-vector operations, you can look at this help assignment.

#-------------------------------------------------------------------------------------------------------------------
print('Group members:')
print()
# Group members

print('Oystein Falkeid')
print('e-mail: oystein.falkeid@nmbu.no')
print()
print('Eirik Mentyjaervi')
print('e-mail: eirik.mentyjarvi@nmbu.no')   
print()                  

import numpy as np # henter numpy til å brukes i oppgavene

#-------------------------------------------------------------------------------------------------------------------

# Task 0: Warmup exercise (0 points)
# In this exercise, you will implement two functions that perform vector addition. 
# A vector can be represented as a list of numbers in Python (e.g., [1, 2, 3]).

# Define a function called inplace_add_vectors(vec1, vec2):

# 1 This function should add the corresponding elements of vec2 to vec1.
# After calling this function, vec1 should be modified to hold the sum of the two vectors.

# Example:
# v1 = [1, 2, 3]
# v2 = [4, 5, 6]
# inplace_add_vectors(v1, v2)
# print(v1) # Output: [5, 7, 9]

# 2 Define a function called add_vectors(vec1, vec2):

# This function should return a new vector where each element is the sum of the corresponding elements from vec1 and vec2.
# The input vectors (vec1 and vec2) should remain unchanged.

# Example:
# v1 = [1, 2, 3]
# v2 = [4, 5, 6]
# v3 = add_vectors(v1, v2)
# print(v1) # Output: [1, 2, 3]
# print(v3) # Output: [5, 7, 9]

# If you want to check your solution or need help, take a look at this video.

#-------------------------------------------------------------------------------------------------------------------
print('Task 0: Warmup exercise (0 points)')
print()








print()
#-------------------------------------------------------------------------------------------------------------------
# Task 1: Matrix operations (2 points)

# * Create a large matrix:

# Make a 2D NumPy array of size 5000X5000, filled with random integers between 0 and 100.

# * Write four functions to work with the matrix:

#   1 Mean function: Write a function that calculates the average (mean) of all the numbers in the matrix. 
#       (Hint: The mean is the sum of all array entries divided by the total number of entries.)

#   2 Variance function: Write a function to calculate the variance of the matrix. 
#       (Hint: The variance measures how much the entries in the matrix differ from the mean. 
#       It's calculated as the average of the squared differences from the mean, i.e., where 
#       and are the array entries (or matrix entries).)

#   3 Sum function: Write a function that returns the total sum of all numbers in the matrix.

#   4 Multiply function: Write a function that returns a new matrix where each number in the input matrix is multiplied by a given number.
# 
# * Important Notes:

# The input matrix should not be changed.
# Be efficient in your implementation to avoid slowing down the program (for example, avoid unnecessary memory use or operations that slow down access to the matrix. Use concepts discussed in the lecture.)
# Write the code for these functions yourself—don’t use built-in functions from libraries for the calculations.

#-------------------------------------------------------------------------------------------------------------------
print('Task 1: Matrix operations (2 points)')
print()








print()
#-------------------------------------------------------------------------------------------------------------------

# Task 2: Stencil matrix (3 points)
# Create a stencil matrix of the form


# with 50 by 50 entries. That is, create a matrix with diagonal entries of -2 and off-diagonal entries (the entries left and right of the diagonal) of 1. The first row is 
# , i.e., the left off-diagonal entry is missing. The last row is 
# , i.e., the right off-diagonal entry is missing.

# We now want to compute the dominant eigenvalue of this matrix. An eigenvalue tells you how a matrix will change certain vectors through multiplication. If you do not know what an eigenvalue is, that is no problem and this knowledge is not required to solve this task. If you wish to get a better understanding, you can watch this videoLinks to an external site. and the videos in this series, but this is really not required. To compute the dominant eigenvalue, take a random vector 
#  with 50 entries and multiply it by 
# , leading to 
# . Set 
#  and repeat the process. That is, with our new 
# , compute 
# , set 
#  and proceed. You can use numpy functionality to compute multiplications and norms.  After 100 iterations, print out the value of 
#  which approximates the dominant eigenvalue. Check the result by computing Lambda, V = np.linalg.eig(A) and inspecting the largest absolute value in Lambda.

#-------------------------------------------------------------------------------------------------------------------
print('Task 2: Stencil matrix (3 points)')
print()








print()
#-------------------------------------------------------------------------------------------------------------------

# Task 3: Challenge exercise (0 points)
# Try to rewrite task 2 so that you never have to store the matrix 
# . For this, write your own function multiply_efficient(v), which computes the matrix-vector product without requiring the matrix. To write this function, think about the operations that will be performed when computing 
#  and check if some of these operations can be left out for our choice of 
# . Hint: A lot of entries in 
#  are zero!

#-------------------------------------------------------------------------------------------------------------------
print('Task 3: Challenge exercise (0 points)')
print()








print()