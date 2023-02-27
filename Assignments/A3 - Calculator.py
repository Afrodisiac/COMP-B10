# A3 - Calculator by Jeremy Stretter
# COMP B10
# Professor Moseley
# Spring 2023
# 2/7/2023

# Constraints:
    # You must use at least 2 numbers input by the user.
    # Calculator must output the correct answer, in the correct format.
    # You must perform the math/calculations.
    # string.format() should be used to format the final number.
    # Use only what we have covered so far in class.
    # Each line in the code should be commented with a brief explanation.

# Welcome messaage
print("A3 - BMI Calculator by Jeremy Stretter\n")

# Variables
strUser_Name = input("What is your name?\n")  # Asks user for name
intUser_Height = int(input("How tall are you (in inches)?\n"))  # Asks user for height, in inches
intUser_Weight = int(input("How much do you weigh?\n"))  # Asks user their weight
strUser_BMI = (intUser_Weight * 703) / (intUser_Height ** 2)  # Weight is multiplied by 703 to convert lbs to kgs

# Program
if strUser_BMI < 18.5:
    # Uses if statement to check if strUser_BMI is less than 18.5; prints to console
    print(f"Uh-oh, {strUser_Name}! According to the math, your BMI is {strUser_BMI}, which classifies you as Underweight!")

elif 18.5 < strUser_BMI < 24.9:
    # Uses double-if statement to check if strUser_BMI is less than 18.5 AND 24.9; prints to console
    print(f"{strUser_Name}, your BMI is {strUser_BMI}, which classifies you as Normal. Nothing more, normie.")

elif 24.9 < strUser_BMI < 29.9:
    # Uses double-if statement to check if strUser_BMI is less than 24.9 AND 29.9; prints to console
    print(f"Careful, {strUser_Name}. Your BMI was calculated at {strUser_BMI}, which is considered Overweight.")

elif strUser_BMI > 29.9:
    # Uses if statement to check if strUser_BMI is greater than 29.9; prints to console
    print(f"{strUser_Name}, your BMI is {strUser_BMI}, which is considered Obese. Please see a physician.")