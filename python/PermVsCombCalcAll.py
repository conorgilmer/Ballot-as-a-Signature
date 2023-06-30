#!/usr/bin/env python
# coding: utf-8

import math

# Get User Input
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        print("No.. input is not a number. It's a string")

# Calculate Permutation nPr
def permCalc(n,r):
    perm = int((math.factorial(n)/(math.factorial(n-r))))
    return perm

# Calculate Combination nCr
def combiCalc(n,r):
    combi = int((math.factorial(n)/(math.factorial(n-r))) * math.factorial(r))
    return combi


# Main Program

# input values for n and r and calculate nPr    
N = input("Enter the number of candidates(n) > ")
check_user_input(N)
n= int(N)

#Print all Permutations for n candidates
print("Print all Permutations for "+ str(n) + " candidates")
print("r\tPermutations\tCombinations")
for r in range(1,n+1):
    perms = permCalc(n,r)
    combi = combiCalc(n,r)
    print("%d \t %d \t %d" % (r, perms, combi))




