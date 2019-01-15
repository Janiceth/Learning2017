# -*- coding:utf-8 -*-
# __author__ = ‘Janice’
# __project__  = ‘PyTest’

# !/usr/bin/env python3
sticks = 21
print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will loose")

While True:
        print("Sticks left: ", sticks)
        sticks_taken = int(input("Please take sticks(1-4):"))
        if sticks == 1:
                print("You took the last stick, you loose")
        if sticks_taken >=5 or sticks_taken <=0:
                print("Wrong choice")
                continue
        print("Computer took: ", (5 - sticks_taken), "\n")
        sticks -= 5