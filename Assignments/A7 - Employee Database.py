# A7 - Employee Database
# COMP B10
# Professor Moseley
# Spring 2023
# 3/18/23

# Constraints:
# Use nested dictionaries and custom functions to create an employee database
# program that allows you to add and remove employee records.
# It should include name, salary, and position title information for each employee.

# Ideas:
# - Authentication
# - User logged in with lowest priviliges, see certain data
# - Deleting employee adds to variable to keep history
# - Delete employee record by ID or name
# - Rollback changes to database


# Employee Database
dEmployeeRecs = {
1: {"name": "Lee, Samantha", "title": "Marketing Manager", "salary": "$85,000.00"},
2: {"name": "Patel, Eric", "title": "Software Engineer", "salary": "$95,000.00"},
3: {"name": "Johnson, Sarah", "title": "HR Coordinator", "salary": "$55,000.00"},
4: {"name": "Nguyen, Michael", "title": "Accountant", "salary": "$75,000.00"},
5: {"name": "Davis, Emily", "title": "Graphic Designer", "salary": "$60,000.00.00"},
6: {"name": "Kim, David", "title": "Sales Representative", "salary": "$70,000.00"},
7: {"name": "Hernandez, Amanda", "title": "Customer Service Representative", "salary": "$45,000.00"}
}

# Function to list current employees and their respective information
def listCurrentEmployees():
    print("Here's a list of current employees:")

    # Prints out each employee's ID, name, title, and salary
    for id in dEmployeeRecs:
        print("\nEmployee ID:", id)
        print("Name:", dEmployeeRecs.get(id).get("name"))
        print("Title:", dEmployeeRecs.get(id).get("title"))
        print("Salary:", dEmployeeRecs.get(id).get("salary"))

# Generates new ID for new employee
def getNewID():

    # Creates array of all current IDs
    arrTemp = []

    # Adds each ID to array
    for intKey in dEmployeeRecs:
        arrTemp.append(intKey)

    # Sorts array in descending order
    arrTemp.sort(reverse=True)

    # Returns highest ID + 1
    return arrTemp[0] + 1

# Function to add new employee to current database
def addNewEmployee():
    
    # Asks for user input for employee's name, title, and salary
    strEmployeeName = input("\nEnter the employee's name: ")
    strEmployeeTitle = input("\nEnter the employee's title: ")

    # Checks if user input is a valid number before continuing
    try:
        floatEmployeeSalary = input("\nEnter the employee's salary: ")
    except ValueError:
        print("Please enter a valid number for the employee's salary.")
    
    # Formats provided salary to USD currency format
    floatSalaryFormatted = "${:,.2f}".format(float(floatEmployeeSalary.replace("$", "").replace(",", "")))

    # Adds id to employee dictionary entry
    intID = getNewID()

    # Parses data into structure appropriate for database
    dNewEmployee = {"name": strEmployeeName, "title": strEmployeeTitle, "salary": floatSalaryFormatted}

    # Adds new employee to database
    dEmployeeRecs[intID] = dNewEmployee
    print("Employee successfully added to database.")
    listCurrentEmployees()

# Function to remove employee from current database
def removeEmployeeRec():
    
    # Lists current employee list
    listCurrentEmployees()

    # Prompts user which employee
    try:
        intChoice = int(input("\nEnter the ID of the employee you wish to remove: "))
    except ValueError:
        print("Please enter the employee ID, e.g. 1 for Lee, Samantha.")

    # Removes the employee from the database, shows user which employee was removed, and shows updated database
    dRemovedEmployee = dEmployeeRecs.pop(intChoice)
    print(f"You have successfully removed {dRemovedEmployee} from the database.")
    print("Here is the updated list of employees:")
    listCurrentEmployees()


# Welcome message/UI
print("#" * 80)
print("#" * 9, " " * 60, "#" * 9)
print("#" * 9, "Employee Records Database".center(60), "#" * 9)
print("#" * 9, " " * 60, "#" * 9)
print("#" * 80)
print("\n")

# Main Program Loop
while(True):

    try:
        intInputChoice = int(input("What would you like to do?\n1) View current employees\n2) Add new emplopyee to database \
            \n3) Remove employee from database\n\n"))
            
        if intInputChoice in (1, 2, 3):
            if intInputChoice == 1:
                listCurrentEmployees()
            elif intInputChoice == 2:
                addNewEmployee()
            elif intInputChoice == 3:
                removeEmployeeRec()
        else:
            pass

        strAnotherTransaction = input("\nWould you like to do something else: (y)es or (n)o?\n".lower())
        if strAnotherTransaction == "n":
            print("\nGoodbye.")
            break
        else:
            continue

    except ValueError:
        print("Please make a valid selection.")
        continue

    