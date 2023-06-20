#!/usr/bin/env python
# coding: utf-8
# Quota(Q) in a PR-STV Election
# V = total number of votes
# S = number of seats to allocate
# The Droop Quota is
# Q = (V/S+1) + 1
# The Hare Quota is
# Q = (V/S)

import math

#Check an integer has been inputted
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
        return(val)
    except ValueError:
        print("No.. input is not a number. It's a string")

#Main Programm
V = input("Enter in the valid number of votes ")
v = check_user_input(V)
S = input("Enter in the number of seats to allocate ")
s = check_user_input(S)
Q = (v/s)
print("the Hare Quota is ",Q) 
Q = round((v/(s+1))+1)
print("the Droop Quota is ",Q) 
