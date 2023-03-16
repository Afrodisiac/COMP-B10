# A5 - ATM Program by Jeremy Stretter
# COMP B10
# Professor Moseley
# Spring 2023
# 3/12/2023

# Constraints:
    # The game should be player vs. computer
    # There should be at least one function used in your code.
    # The game should go through up to three rounds,
    # and declare the winner after either the computer or the player wins 2 rounds.
    # After a winner is declared, the program should ask if the user wants to play another game.


# Imports random module
import random

# Welcome message/UI
print("#" * 80)
print("#" * 9, " " * 60, "#" * 9)
print("#" * 9, "Rock, Paper, Scissors".center(60), "#" * 9)
print("#" * 9, " " * 60, "#" * 9)
print("#" * 80)
print("\n")

# Global variables that intialize and maintain scores
intPlayerScore = 0
intComputerScore = 0

# Variable to define legal moves/inputs for player 
dictLegalMoves = {'r' : 'rock', 'p' : 'paper', 's' : 'scissors'}

# Function that utilizes random module, generates choice for Computer player
def computerChoice():
    strComputerChoice = ("r", "p", "s")
    return random.choice(strComputerChoice)

# Function that asks for user choice and sets it to a variable
def userChoice():
    strUserChoice = input("(R)ock, (p)aper, or (s)cissors: ").lower()

    # If user input is not valid, asks for input again
    if strUserChoice not in ("r", "p", "s"):
        print("Invalid input. Please try again.")
        userChoice()
    return strUserChoice

# Function that decides who won
def gameReferee(strComputerChoice, strUserChoice):
    
    # If both players make the same play, results in a tie
    if strUserChoice in ("r", "p", "s") and strComputerChoice == strUserChoice:
        return "Tie"

    else:
        if strUserChoice == "r":
            if strComputerChoice == "p":
                print(f"Computer chose {dictLegalMoves['p']} and won this round.")
                return "Computer"
            else:
                print(f"You won this round with {dictLegalMoves['r']}, since Computer chose {dictLegalMoves['s']}.")
                return "Player 1"

        elif strUserChoice == "p":
            if strComputerChoice == "s":
                print(f"Computer chose {dictLegalMoves['s']} and won this round.")
                return "Computer"
            else:
                print(f"You won this round with {dictLegalMoves['p']}, since Computer chose {dictLegalMoves['r']}.")
                return "Player 1"

        elif strUserChoice == "s":
            if strComputerChoice == "r":
                print(f"Computer chose {dictLegalMoves['r']} and won this round.")
                return "Computer"
            else:
                print(f"You won this round with {dictLegalMoves['s']}, since Computer chose {dictLegalMoves['p']}.")
                return "Player 1"

# Funtion that prints current scores for both players
def gameScore():
    print("Current Score:")
    print(f"Player 1: {intPlayerScore} | Computer: {intComputerScore}")

# Asks user if they want to play another game
while True:

    # Main game loop that runs until a player reaches 2 points
    while True:
        strWinner = gameReferee(computerChoice(), userChoice())

        if strWinner == "Player 1":
            intPlayerScore += 1
        elif strWinner == "Computer":
            intComputerScore += 1
        else:
            print(f"It's a tie -- no points awarded.")
        
        gameScore()

        if intPlayerScore >= 2:
            print("Player 1 won the game!")
            break
        elif intComputerScore >= 2:
            print("Computer won the game!")
            break
    
    # Asks user if they want to play another game and resets scores
    strPlayAgain = input("Would you like to play again? (y/n): ").lower()
    if strPlayAgain == "y":
        intPlayerScore = 0
        intComputerScore = 0
        continue
    else:
        print("Thanks for playing!")
        break