from datetime import datetime

PROMPT = "What would you like to do?\n" \
         "0. Stop\n" \
         "1. Create Account\n" \
         "2. Add a Friend\n" \
         "3. Create a Post\n" \
         "4. See All of the User's Friends' Posts\n" \
         "5. Suggest friends"

class Database():

    def __init__(self):
        self.users = []
        self.posts = []

    #Error Checking
    def add_user(self, user):
        self.users.append(user)

    def add_post(self, post):
        self.posts.append(post)

    def get_user(self,email):
        return next(user for user in self.users if user.email == email)

    def __str__(self):
        return str(self.__dict__)

class Post():

    def __init__(self, text, timestamp, poster):
        self.text = text
        self.timestamp = timestamp
        self.poster = poster

    def __str__(self):
        return str(self.__dict__)

class User():

    def __init__(self, name, password, age, email):
        self.name = name
        self.password = password
        self.age = age
        self.email = email
        self.posts = []
        self.friends = []

    def add_friend(self, friend):
        if not isinstance(friend, User):
            raise ValueError("Cannot add non-User friend")
        self.friends.append(friend)

    def add_post(self, post):
        if not isinstance(post, Post):
            raise ValueError("Cannot add non-Post value")
        self.posts.append(post)

    def __str__(self):
        return str(self.__dict__)

#2birdz, 1stone
def add_post(user, post, db):
    user.add_post(post)
    db.add_post(post)

def friends_posts(user, db):
    friends = [u.name for u in user.friends]
    posts = [p for p in db.posts if p.poster in friends]
    return posts

# function to read friends.txt
def read_file(filename):
    db = Database()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            stuff = line.strip().split(',')
            if len(stuff) > 2:
                name = stuff[0]
                age = stuff[1]
                password = stuff[2]
                email = stuff[3]

                user = User(name, password, age, email)
                db.add_user(user)
            else:
                email = stuff[0]
                femail = stuff[1]

                user = db.get_user(email)
                friend = db.get_user(femail)

                user.add_friend(friend)

    print(user.__dict__)
    print(friend.__dict__)

def suggest_friends(user, db):
    friends = [u.handle for u in user.friends]
    friends_friend = [friend for friend in db.users if friend.name in friends]

    friend_list = []

    for friend in friends_friend:
        friend_list.append(friend.friends)

        suggested_friends = []

        for x in friend_list:
            if x not in suggested_friends:
                suggested_friends.append(x)

        for x in suggested_friends:
            for peeps in x:
                print(peeps.name)
    return suggested_friends




def main():
    #Create a db to store the user
    db = Database()
    read_file("Friends.txt")

    #Prompt the user for what they would like to do in the application
    print(PROMPT)
    choice = input("Choice: ")

    while choice != '0':
        #Idiotproof for invalid inputs
        while choice not in ('0', '1', '2', '3', '4', '5'):
            choice = input("Choice: ")

        #Grab enough users to prevent many errors
        while len(db.users) < 2 and choice not in ('1'):
            # Create an account
            print("System needs more users...")
            print("Create an account: ")
            name = input("Name: ")
            email = input("Email: ")
            list = [user for user in db.users if user.email == email]

            # Handle unique declaration of emails
            while len(list) > 0:
                print("ERROR: Email taken: ")
                email = input("Re-enter email: ")
                list = [user for user in db.users if user.email == email]

            password = input("Password: ")
            age = input("Age: ")

            user = User(name, password, age, email)
            db.add_user(user)

        # Create an account
        if choice == '1':
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            age = input("Age: ")

            user = User(name, password, age, email)
            db.add_user(user)

        # Add a Friend
        elif choice == '2':
            # Email to grab user
            email = input("Enter the user's email for adding a friend: ")

            # Email to grab friend
            femail = input("Enter the friend's email who will be added: ")

            # Add a friend
            user = db.get_user(email)
            friend = db.get_user(femail)

            user.add_friend(friend)

            # For printing out the user after the add
            print(user.__dict__)
            print(friend.__dict__)

        # Post
        elif choice == '3':
            # Enter the email of the user to get their name and pass that to post
            email = input("Enter the email of the user creating the post: ")
            user = db.get_user(email)
            post = Post(input("Message: "), datetime.now(), user.name)

            #We use this method "secret method" instead of calling both classes add_post method
            add_post(user, post, db)

            #For printing out the user after the add
            print(user.__dict__)

        #See friends posts
        elif choice == '4':
            email = input("Enter the email of the user to see their friends' posts: ")
            user = db.get_user(email)

            #This call calls the method and returns the friends' posts
            friends_posts(user, db)

            #For printing out the user after the add
            print(user.__dict__)

        #choice for friend suggestion
        elif choice == '5':
            email = input("Enter the email of the user for friends suggestion: ")
            user = db.get_user(email)
            suggest_friends(user,db)


        #Prompt the user for what they would like to do in the application
        print(PROMPT)
        choice = input("Enter next choice: ")

if __name__ == '__main__':
    main()
