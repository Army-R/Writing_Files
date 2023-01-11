#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:15:35 2021

@author: Army-R
"""
# Append vs write mode 

file = open("new_team7.txt", "w")

new_team = ["Boruto \n", "Mitsuki \n", "Kawaki \n"]
new_leader = "Konohamaru \n"

file.write(new_leader)
file.writelines(new_team)

file.close()

# Append-adds at last
file = open("new_team7.txt", "a")
file.write("This are the new team 7, sons of first team \n")
file.close()

file = open("new_team7.txt", "r")
print("output of Readlines after appending")
print(file.read())
print()
file.close()

# Write-Overwrites
file = open("new_team7.txt", "w")
file.write("The new team is from Boruto show \n")
file.close()

file = open("new_team7.txt", "r")
print("Output of Readlines after writing")
print(file.read())
print()
file.close()
