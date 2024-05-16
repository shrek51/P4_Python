from os import *
from sys import *
from collections import *
from math import *

def constructMatrix(n, m):
    # Store given number of rows and columns for later use
    r = n
    c = m

    # Initialize the character to be stored in a[][]
    x = 'X'
    
    # A 2D array to store the output to be printed
    a = [[None] * m for _ in range(n)] 

    # Fill characters in a[][] in spiral form
    # Every iteration fills one rectangle of either Xs or Os 
    i, k, l = 0, 0, 0
    while k < m and l < n:
        # Fill the first row from the remaining rows
        for i in range(l, m):
            a[k][i] = x 
        k += 1
 
        # Fill the last column from the remaining columns
        for i in range(k, n):
            a[i][m - 1] = x 
        m -= 1
 
        # Fill the last row from the remaining rows 
        if k < n:
            for i in range(m - 1, l - 1, -1):
                a[n - 1][i] = x 
            n -= 1
 
        # Print the first column from the remaining columns 
        if l < m:
            for i in range(n - 1, k - 1, -1):
                a[i][l] = x 
            l += 1
 
        # Flip character for next iteration
        x = 'X' if x == '0' else '0'

    # Return the filled matrix
    return a