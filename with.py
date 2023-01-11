#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:33:19 2021

@author: Army-R
"""

# With statement
team_members = ["Choji \n", "Shikamaru \n", "Ino \n"]

# Writing to file
with open("team10.txt", "w") as file:
    # Writing data to a file
    file.write("Asuma \n")
    file.writelines(team_members)
    
# Reading from file
with open("team10.txt", "r+") as file:
    # Reading from a file
    print(file.read())
    
