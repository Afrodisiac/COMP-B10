'''
# A5 - ATM Program by Jeremy Stretter
# COMP B10
# Professor Moseley
# Spring 2023
# 2/22/2023

# Constraints:
#   The balance cannot go below zero, so make sure you prevent that.
#   use string.rjust() as needed to make sure numbers line up properly.
#   Make the UI look good.
#   After each transaction, ask the user if they want to make another transaction.
#   Make sure you keep track of the amount in each account while the program runs.
#   Start each account with some $$.
'''


# Starting balances--DO NOT TOUCH!
FLOATCHKBAL = 420.69
FLOATSAVBAL = 86753.09


# Welcome message/UI
print("#" * 80)
print("#" * 9, " " * 60, "#" * 9)
print("#" * 9, "Welcome to Spark Joint Capital ATM".center(60), "#" * 9)
print("#" * 9, " " * 60, "#" * 9)
print("#" * 80)
print("\n")

# Get user's name and assigns to a variable
strUser_Name = input("It seems that you are a new user. Please enter your name below:\n")
print(f"\nHi, {strUser_Name}! It is currently 69° on the West Coast.\n")

# Program
while True:
    strUserChoice = input(f"\nWhat would you like to do today, {strUser_Name}?\n\n(T)ransfer funds\n(B)alance inquiry\n(F)ast cash\n(C)ash deposit\n")
    # User selects Transfer Funds option
    if strUserChoice in ("T", "t"):
        # Confirms which account is being funded
        strTrans_Funds = input("\nOkay, you want to transfer funds. Which account are you you transferring from?\n(C)heckings\n(S)avings\n")
        # Transfer from Checking
        if strTrans_Funds in ("C", "c"):
            # Provides current balance of Checkings account; asks how much to transfer
            floatTrans_Funds_Amt_Chk = input(f"\nCurrent Checkings balance is {FLOATCHKBAL}. How much would you like to transfer?\n")
            # Converts str to float
            floatTrans_Funds_Amt_Chk = float(floatTrans_Funds_Amt_Chk)
            # Verifies entered amount is available in the account
            if floatTrans_Funds_Amt_Chk <= FLOATCHKBAL:
                FLOATCHKBAL -= floatTrans_Funds_Amt_Chk
                FLOATSAVBAL += floatTrans_Funds_Amt_Chk
                print("\nHere are your updated balances:\n")
                print("Checkings:".ljust(20), str(FLOATCHKBAL).rjust(20))
                print("Savings:".ljust(20), str(FLOATSAVBAL).rjust(20))

            # If entered amount exceeds available balance, prints error message
            else:
                print("Sorry, that amount exceeds the available balance of this account.")
                continue
            
            # Another transaction
            strAnotherTrans = input("Would you like to make another transaction: (Y)es or (n)o?\n")
            if strAnotherTrans in ("Y", "y"):
                continue
            # User does not want to make another transaction
            else:
                print("Thank you for choosing Spark Joint Capital. Have a lifted day!")
                break
        
        # Transfer from Checking
        elif strTrans_Funds in ("S", "s"):
            # Provides current balance of Savings account; asks how much to transfer
            floatTrans_Funds_Amt_Sav= input(f"\nCurrent Savings balance is {FLOATSAVBAL}. How much would you like to transfer?\n")
            # Converts str to float
            floatTrans_Funds_Amt_Sav = float(floatTrans_Funds_Amt_Sav)
            # Verifies entered amount is available in the account, then transfers funds
            if floatTrans_Funds_Amt_Sav <= FLOATSAVBAL:
                FLOATSAVBAL -= floatTrans_Funds_Amt_Sav
                FLOATCHKBAL += floatTrans_Funds_Amt_Sav
                print("\nHere are your updated balances:\n")
                print("Checkings:".ljust(20), str(FLOATCHKBAL).rjust(20))
                print("Savings:".ljust(20), str(FLOATSAVBAL).rjust(20))

            # If entered amount exceeds available balance, prints error message
            else:
                print("Sorry, that amount exceeds the available balance of this account.")
                continue
        
            # Another transaction
            strAnotherTrans = input("Would you like to make another transaction: (Y)es or (n)o?\n")
            if strAnotherTrans in ("Y", "y"):
                continue
            # User does not want to make another transaction
            else:
                print("Thank you for choosing Spark Joint Capital. Have a lifted day!")
                break

    # User selects Balance Inquiry option
    elif strUserChoice in ("B", "b"):
        # Confirms which account is being checked
        strUser_Bal_Choice = input("Which account would you like to check the balance of: (C)heckings or (S)avings?\n")
        # Prints balance of Checkings account
        if strUser_Bal_Choice in ("C", "c"):
            print("As of today, the current balance of your Checkings account is:".ljust(20), str(FLOATCHKBAL).rjust(20))
        # Prints balance of Savings account
        elif strUser_Bal_Choice in ("S", "s"):
            print("As of today, the current balance of your Savings account is:".ljust(20), str(FLOATSAVBAL).rjust(20))
        # Invalid input
        else:
            print("Invalid input--please try again.")
            continue
        
        # Another transaction
        strAnotherTrans = input("Would you like to make another transaction: (Y)es or (n)o?\n")
        if strAnotherTrans in ("Y", "y"):
            continue
        # User does not want to make another transaction
        else:
            print("Thank you for choosing Spark Joint Capital. Have a lifted day!")
            break

    # User selects Fast Cash option
    elif strUserChoice in ("F", "f"):
        # Confirms which account is being withdrawn from
        strUser_Fast_Cash_Acct = input("Which account would you like to withdraw from: (C)heckings or (S)avings?\n")
        # Confirms amount to withdraw
        strUser_Fast_Cash_Amt = input("How much would you like to withdraw?\n")
        # Converts str to float
        floatUser_Fast_Cash_Amt = float(strUser_Fast_Cash_Amt)
        # Withdraws funds from Checkings account
        if strUser_Fast_Cash_Acct in ("C", "c"):
            FLOATCHKBAL -= floatUser_Fast_Cash_Amt
            print("Your new Checkings balance is:".ljust(20), str(FLOATCHKBAL).rjust(20))
            print("Please take your cash from the dispenser below. Have a lifted day!")
        # Withdraws funds from Savings account
        elif strUser_Fast_Cash_Acct in ("S", "s"):
            FLOATSAVBAL -= floatUser_Fast_Cash_Amt
            print("Your new Savings balance is:".ljust(20), str(FLOATSAVBAL).rjust(20))
            print("Please take your cash from the dispenser below. Have a lifted day!")
        # Invalid input
        else:
            print("Invalid input--please try again.")
            continue

        # Another transaction
        strAnotherTrans = input("Would you like to make another transaction: (Y)es or (n)o?\n")
        if strAnotherTrans in ("Y", "y"):
            continue
        # User does not want to make another transaction
        else:
            print("Thank you for choosing Spark Joint Capital. Have a lifted day!")
            break
  
    # User selects Cash Deposit option
    elif strUserChoice in ("C", "c"):
        # Confirms which account is being deposited into
        strUser_Deposit = input("Which account would you like to deposit into: (C)heckings or (S)avings?\n")
        # Confirms amount to deposit
        strUser_Deposit_Amt = input("How much would you like to deposit?\n")
        # Converts str to float
        floatUser_Deposit_Amt = float(strUser_Deposit_Amt)
        # Deposits funds into Checkings account
        if strUser_Deposit in ("C", "c"):
            FLOATCHKBAL += floatUser_Deposit_Amt
            print("Your new Checkings balance is:".ljust(20), str(FLOATCHKBAL).rjust(20))
            print("Thank you for your deposit. Have a lifted day!")
        # Deposits funds into Savings account
        elif strUser_Deposit in ("S", "s"):
            FLOATSAVBAL += floatUser_Deposit_Amt
            print("Your new Savings balance is:".ljust(20), str(FLOATSAVBAL).rjust(20))
            print("Thank you for your deposit. Have a lifted day!")
        # Invalid input
        else:
            print("Invalid input--please try again.")
            continue

        # Another transaction
        strAnotherTrans = input("Would you like to make another transaction: (Y)es or (n)o?\n")
        if strAnotherTrans in ("Y", "y"):
            continue
        # User does not want to make another transaction
        else:
            print("Thank you for choosing Spark Joint Capital. Have a lifted day!")
            break
