# -*- coding: utf-8 -*-
"""
ICS 111 Intro to Computer Science I
GICP 3.2 For Loops
f08_conversions.py
Christi Palacat
September 16, 2018
"""
# Initialize value for iteration loop
decimal=0

#Assigning value to a variable in order to indicate where extra tab needs to be added
tab= 7

# Print header title
print('\tdecimal\tbinary\t\thex')

#For loop counting from 0 to 31
for decimal in range (0,32):
    
#Statement where extra tab is added for decimal of 0-7 for hex to align    
    if decimal<=tab:
        print('\t',decimal,'\t',bin(decimal),'\t','\t',hex(decimal))
    else:
        print('\t',decimal,'\t',bin(decimal),'\t',hex(decimal))
