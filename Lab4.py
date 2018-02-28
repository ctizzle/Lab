# Author:Charlie Ta

# Project: Lab 4

#Global Variables

users = {}
courses = {}
MAX = 2
available_courses = ('C1', 'C2', 'C3')


#Store User Function for Option 1
def store_user(p1, p2, p3):
    users[p1] = (p2,p3)

#Add User Function for Option 1
def get_input():
    #Prompt for name
    name = input("Enter person's name: ")

    # Prompt for username
    username = input("Enter a username: ")

    # Check to see if username is taken
    while username in users.keys():
        print("This username is already taken.")
        username = input("Enter a username: ")

    #Prompt for password
    password = input("Enter a password: ")
    pass_verify = input("Enter the password again: ")

    #Check to see if passwords are equal
    while password != pass_verify:
        print("The passwords did not match! Try again.")
        password = input("Enter a password: ")
        pass_verify = input("Enter the password again: ")



    #Store information into dictionary
    store_user(username, name, password)

    print(users)

#Login Security Check Function for Option 2
def login(username, password):
    if password == users[username][1]:
        return True


#Enroll Course Function for Option 2
def enroll_course(username,course):
    courses[username] = list()
    courses[username].append(course)
    print(courses)

#Function to find which course has the most students enrolled
def get_max_enrollment():
    enrolled = {}
    for courses_list in courses.values():
        for course in courses_list:
            if course not in enrolled.keys():
                enrolled[course] = 1
            else:
                enrolled[course] += 1

    values = list(enrolled.values())
    keys = list(enrolled.keys())
    max_enrolled = max(values)
    placement = values.index(max_enrolled)
    return keys[placement]


def main():
    #User Prompt
    choice = input("What would you like to do?\n0. Stop\n1. Add a User\n2. Enroll a User in a Course\n3. Determine Class with Most Students Enrolled\n")
    #Program as the user doesn't pick STOP
    while choice != '0':
        #Error Checking
        while choice not in ('0', '1', '2', '3'):
            choice = input("NOT A VALID CHOICE! What would you like to do?\n0. Stop\n1. Add a User\n2. Enroll a User in a Course\n3. Determine Class with Most Students Enrolled\n")

        #Add user option
        if choice == '1':
            get_input()

        #Enroll in a course option
        elif choice == '2':
            username = input("What is your username? ")
            while username not in users.keys():
                print("That username is not in our system!")
                username = input("What is your username? ")
            password = input("What is your password? ")

            tries = 0
            while not login(username, password) and tries < MAX:
                print("Login failed! Try again.")
                password = input("What is your password? ")
                tries += 1
            if tries == MAX:
                print("You have exceeded the number of tries to login.")

            if login(username,password):
                course = input("What course would you like to enroll in? ")
                if course not in available_courses:
                    print("That is not an available course.")
                    course = input("What course would you like to enroll in? ")
                enroll_course(username, course)

        #Most students enrolled option
        elif choice == '3':
            max_course = get_max_enrollment()
            print("%s has the most students" % max_course)

        #Re-Prompt
        choice = input("What would you like to do?\n0. Stop\n1. Add a User\n2. Enroll a User in a Course\n3. Determine Class with Most Students Enrolled\n")


if __name__ == "__main__":
    main()
