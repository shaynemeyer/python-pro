from statistics import mean as m

admins = {'admin': 'admin'}

gradeDict = {'Kelly': [91, 90], 'John': [89, 90]}


def enter_grades():
    addName = input("Student name: ")
    addGrade = input("Student grade: ")

    if addName in gradeDict:
        print("Adding grade...")
        gradeDict[addName].append(float(addGrade))
        print(gradeDict)
    else:
        print("Student doesn't exist!")


def remove_student():
    delName = input("Enter a name to delete. ")
    if delName in gradeDict:
        print("Removing student...")
        del gradeDict[delName]

    print(gradeDict)


def student_AVGs():
    for eachStudent in gradeDict:
        gradeList = gradeDict[eachStudent]
        avgGrade = m(gradeList)
        print(eachStudent, 'has an average grade of', avgGrade)


def main():
    print('''
    Welcome to Grade Central

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    ''')

    menuItem = input("What would you like to do today? (Enter a number)")

    if menuItem == '1':
        enter_grades()
    elif menuItem == '2':
        remove_student()
    elif menuItem == '3':
        student_AVGs()
    elif menuItem == '4':
        exit()
    else:
        print('You entered a number that is not available. Try again.')


login = input("Username: ")

if login in admins:
    passw = input('Password: ')

    if admins[login] == passw:
        print("Welcome", login)
        while True:
            main()
    else:
        print("Invalid password!")
else:
    print("Invalid username!")
