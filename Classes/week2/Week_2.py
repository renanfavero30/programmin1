"""
Author: Lisha Zhou - Professor
Version: class - week 2
Description: input and output
Date: 01/19/2023
"""


# Preparation for the QUIZ 1  -  1/18/2023

hourly_wage = input("Enter hourly wage: ")  # store as 10101010
hours_per_week = 8

# convert string "10101" to be an integer using int() function
print("Weekly salary is", int(hourly_wage) * hours_per_week)  # we canot concatenate differt types of variables

weekly_pay= int(hours_per_week) * 4 # this is the conversiont
print(weekly_pay)


a = [1, 2, 3] * 4
print(a)