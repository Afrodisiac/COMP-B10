# A2 - Mad Libs Assignment by Jeremy Stretter
# COMP B10
# Professor Moseley
# Spring 2023
# 2/3/2023

# Imports
from termcolor import colored, cprint

# Welcomes user to program/script
cprint("A2 - Mad Libs Assignment by Jeremy Stretter\n", "cyan")

# Global variables
strFruit = colored(input("Enter a fruit: "), "yellow")
strNoun = colored(input("Enter a place: "), "yellow")
strName = colored(input("Enter a name: "), "yellow")
strAdjective1 = colored(input("Enter an adjective: "), "yellow")
strColor = colored(input("Enter a color: "), "yellow")
strAdjective2 = colored(input("Enter another adjective: "), "yellow")

# Places variables and prints text to console
print("\n")
cprint("*** sung to the tune of Spongebob Squarepants ***\n", "cyan")
print(f"Captain: Ohhh... who lives in a {strFruit} under the {strNoun}?\n\
Kids: {strName} Applebottoms!\n\
Captain: {strAdjective1} and {strColor} and {strAdjective2} is he!\n\
Kids: {strName} Applebottoms! {strName} Applebottoms! {strName} Applebottoms!")