# Charlie Ta
# Lab 8
# ID: 112-62-9632

# Prompt message for user
PROMPT = "What would you like to do?\n" \
         "0. Quit\n" \
         "1. Search for animal\n"

class Animal():

    def __init__(self):
        self.name = ""
        self.age = ""

class Mammal(Animal):

    def __init__(self):
        super(Mammal, self).__init__()
        self.hcolor = ""
        self.region = ""

class Amphibian(Animal):

    def __init__(self):
        super(Amphibian, self).__init__()
        self.water = ""

class Lion(Mammal):

    def __init__(self):
        super(Lion, self).__init__()
        self.roar = 0

class Monkey(Mammal):

    def __init__(self):
        super(Monkey, self).__init__()
        self.intelligence = ""

class Fish(Amphibian):

    def __init__(self):
        super(Fish, self).__init__()
        self.scalelength = 0.0

class Frog(Amphibian):

    def __init__(self):
        super(Frog, self).__init__()
        self.tadpoletime = 0

# Function that will take the file and create object and attributes
def createObjects(filename):
    objs = [] # empty list for objects
    f = open(filename,'r') # read the file
    for line in f.readlines(): # iterates through each line of the file
        attributes = line.strip().split(',') #takes away any spaces and splits each line wherever there's a comma
        klass = eval(attributes[1].split(':')[1]) # the 2nd after colon. eval is used to store as attributes instead of strings
        attributes.pop(1) # gets rid of class so it won't be part of the attributes
        inst = klass() # assigns the klass/eval function to inst
        for a in attributes: #iterates through each attribute for each line
            splitData = a.split(':') # seperates the attribute pairs wherever there's a colon
            setattr(inst, splitData[0], splitData[1]) # sets all the pairs that have been seperated to be attributes
        objs.append(inst) # adds the newly created attributes into the objs list
    return objs


def main():

    # call the createObjects function
    objs = createObjects("animals.txt")

    # prompt the user
    choice = input(PROMPT)

    while choice != '0':

        # idiotproof the program
        while choice not in ('0', '1'):
            print("ERROR! You did not enter the right choice!")
            choice = input(PROMPT)

        if choice == '1':

            aklass = input("What animal class would you like to search?\n")

            try:
                eval(aklass)
            except ValueError:
                print("This is not an animal class!")


            aattr = input("What attribute would you like to search?\n")

            try:
                eval(aattr)
            except ValueError:
                print("This is not a valid attribute!")


            print([getattr(o,aattr) for o in objs if isinstance(o, eval(aklass)) and hasattr(o, aattr)])


        choice = input(PROMPT)










if __name__ == '__main__':
    main()