# Author:Charlie Ta

# Project: Lab 5

#Global Variables

MAX = 2
available_courses = ('C1', 'C2', 'C3')

#Binary Search Function
def search(left, right, l_, target):
    if right - left <= 0:
        return -1
    mid = int((right - left)/2) + left
    if l_[mid] == target:
        return mid
    if target < l_[mid]:
        return search(left, mid, l_, target)
    if target > l_[mid]:
        return search(mid+1, right, l_, target)

def read_user_dict(filename):
    new_dict = {}
    with open(filename, "r") as file:
        for line in file.readlines():
            items = line.strip().split(',')
            username = items[0]
            name = items[1]
            password = items[2]
            new_dict[username] = (name, password)
    return new_dict

def read_course_dict(filename):
    new_dict = {}
    with open(filename, "r") as file:
        for line in file.readlines():
            items = line.strip().split(',')
            username = items[0]
            courses = items[1:]
            new_dict[username] = courses
    return new_dict

def write_user_dict(dictionary, filename):
    with open(filename, "w") as file:
        for key, value in dictionary.items():
            file.write("%s,%s,%s\n"%(key,value[0],value[1]))

def write_course_dict(dictionary, filename):
    with open(filename, "w") as file:
        for key, value in dictionary.items():
            out_str = "%s," % key
            for item in value:
                if(item != ""):
                    out_str += "%s," % item
            print(out_str)
            file.write(out_str+"\n")

#Store User Function for Option 1
def store_user(p1, p2, p3):
    users = read_user_dict("users.txt")
    users[p1] = (p2,p3)
    write_user_dict(users, "users.txt")

    courses = read_course_dict("courses.txt")
    courses[p1] = []
    write_course_dict(courses, "courses.txt")

#Add User Function for Option 1
def get_input():
    #Prompt for name
    name = input("Enter person's name: ")




    #Prompt for password
    password = input("Enter a password: ")
    pass_verify = input("Enter the password again: ")

    #Check to see if passwords are equal
    while password != pass_verify:
        print("The passwords did not match! Try again.")
        password = input("Enter a password: ")
        pass_verify = input("Enter the password again: ")

    # Prompt for username
    username = input("Enter a username: ")

    # Check to see if username is taken
    # while username in users.keys():
    usernames = sorted(list(read_user_dict("users.txt").keys()))
    while search(0, len(usernames), sorted(usernames), username) >= 0:
        print("Username is already taken!")
        username = input("Enter a username: ")


    #Store information into dictionary
    store_user(username, name, password)



#Login Security Check Function for Option 2
def login(username, password):
    users = read_user_dict("users.txt")
    return password == users[username][1]



#Enroll Course Function for Option 2
def enroll_course(username,course):

    courses = read_course_dict("courses.txt")
    courses[username].append(course)
    write_course_dict(courses, "courses.txt")




#Function to find which course has the most students enrolled
def get_max_enrollment():
    enrolled = {}
    course_values = read_course_dict("courses.txt").values()
    for courses_list in course_values:
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
            usernames = sorted(list(read_user_dict("users.txt").keys()))
            while username not in usernames:
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
