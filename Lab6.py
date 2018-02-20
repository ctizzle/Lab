
#Lab 6

from datetime import datetime

#Object for Post
class Post():

    def __init__(self, text, timestamp, user):
        self.text = text
        self.timestamp = timestamp
        self.user = user

#Object for User
class User():

    def __init__(self, name, age, password, email):
        self.name = name
        self.age = age
        self.password = password
        self.email = email
        self.friends = []
        self.posts = []

    #Adds post to posts list
    def post(self, p):
        self.posts.append(p)

    #Adds a friend to friends list
    def add_friends(self, friend):
        self.friends.append(friend)

    def __str__(self):
        return str(self.__dict__)


#Object for Database
class Database():

    def __init__(self):
        self.users = []
        self.posts = []

    #Adds user to database
    def add_user(self, user):
        if not isinstance(user, User):
            raise ValueError("Cannot add non-User type")
        self.users.append(user)

    #Adds post to database
    def add_post(self, post):
        if not isinstance(post, Post):
            raise ValueError("Cannot add non-Post type")
        self.posts.append(post)

    #Used to search for a user
    def get_user(self, email):
        for email in self.users:
            if email in self.users:
                return user in self.users
            else:
                print("No such user!")



    def __str__(self):
        return str(self.__dict__)

def main():

    db = Database()

    #The option prompt for users
    PROMPT = "What would you like to do?\n0. Quit\n1.Create an account\n2.Add a friend\n3.Create a post\n4.See friend's post\n"

    choice = input(PROMPT)

    #User Error
    if choice not in ('0','1','2','3','4'):
        print("Invalid choice! Try again!")
        choice = input(PROMPT)

    #User Choices
    while choice != '0':

        #Option to create account
        if choice == '1':

            user = User(input("What is your name? "), input("What is your age? "), input("What is your password? "), input("What is your email? "))

            db.add_user(user)


        #Option to add a friend
        if choice == '2':
            email1 = input("What is your email? ")
            user = db.get_user(email1)

            email2 = input("What is your friend's email: ")
            new_friend = db.get_user(email2)

            user.add_friends(new_friend)

        #Option to create a post
        if choice == '3':

            post = input("Enter a post: ")
            username = input("Enter username: ")

            new_post = Post(post,datetime.now(),username)

            user.post(new_post)

            db.add_post(new_post)

        #Option to see friend's post
        if choice == '4':
            print("Here are your friends: ")
            print(user.friends)
            friend_selected = input("Whose post would you like to see? ")
            # if friend_selected db.posts in

        choice = input(PROMPT)

    print(db.__dict__)



if __name__ == "__main__":
    main()