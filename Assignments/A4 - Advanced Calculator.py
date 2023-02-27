# A4 - Advanced Calculator by Jeremy Stretter
# COMP B10
# Professor Moseley
# Spring 2023
# 2/8/2023

# Constraints:
#   You must use if statements.
#   There must be at least 2 choices for calculations for the user.


# Variables


# Show UI
print("+" * 80)
print("+" * 9, " " * 60, "+" * 9)
print("+" * 9, "Advanced Calculator".center(60), "+" * 9)
print("+" * 9, "by Jeremy Stretter".center(60), "+" * 9)
print("+" * 9, " " * 60, "+" * 9)
print("+" * 80)
print("\n")

# Main menu
strUser_Choice = input("Which calculation would you like to run?\n 1) Pounds to kilograms \n 2) Kilograms to pounds \n")

# If user chooses option 1, do pounds to kilograms calc.
if strUser_Choice == "1":
    intLbs_to_Kgs = int(input("Enter a weight, in pounds:\n"))  # Variable that stores the user's input
    print((intLbs_to_Kgs), "expressed as kilgrams equals:", intLbs_to_Kgs / 2.2046)  # Prints the result of the math to the console 

# If user chooses option 2, do kilograms to puounds calc.
elif strUser_Choice == "2":
    intKgs_to_Lbs = int(input("Enter a weight, in kilograms:\n"))  # Variabe that stores the user's input
    print((intKgs_to_Lbs), "expressed as pounds equals:", intKgs_to_Lbs * 2.2046)  # Prints the result of the math to the console

# If the user inputs anything else, give error message
else:
    print(f"Unexpected input: expected 1 or 2, got {strUser_Choice} instead. Please rum program again.")  # Prints an error message to the console