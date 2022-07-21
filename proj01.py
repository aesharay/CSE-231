# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 20:57:09 2020

"""
 ###########################################################
     #CSE Project 1
     #define rods
     #convert rods to meters
     #convert meters to feet
     #convert meters to miles
     #convert rods to furlongs
     #calculate minutes per rod
    ###########################################################


#defining user input
rods_str = input("Input rods: ")
rods_float = float(rods_str)
rods_str1 = print("You input" , rods_float , "rods.")

print(" ")
print("Conversions")

#meters
meters_float = rods_float * 5.0292
print("Meters:" , round(meters_float,3))

#feet
feet_float = meters_float /  0.3048
print("Feet:", round(feet_float,3))

#miles
miles_float = meters_float / 1609.34
print("Miles:", round(miles_float,3))

#furlongs
furlongs_float = rods_float / 40
print("Furlongs:", round(furlongs_float,3))

#minutes to walk
minutes_float = (miles_float / 3.1) * 60
print("Minutes to walk", rods_float, "rods:", round(minutes_float,3))

