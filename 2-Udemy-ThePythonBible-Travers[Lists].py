#Travers.py Check if the element in the list
known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

while True:
    print ("Hi! My name is Travis")
    name = input("What is your name?").strip().capitalize()
    # stripe spaces and capitalize the first letter
    if name in known_users:
        print ("Hello {}! ".format(name))
        #.format(name) add name to string {}
        remove = input("Would you like to be removed from the system? Y/N? ").strip().lower()
        if remove == "y":
            #remove name from the list
            # use del known_users[0] if want to delete element by index
            known_users.remove(name)
        elif remove ==  "n":
            print ("No problem, I didn't want you to leave anyway!")




    else:
        print ( "Hmm I don't think I have you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?:").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print ("No worries, se you around")

# other ways to add something to list A=[1,2,3] A= A + [5,6,7] - add numbers
# A = A + list("BCD")=> A [1,2,3,B,C,D] - add string
# A = A+ list(str(456)) => A [1,2,3,'4','5','6'] - add numbers as strings
# A = A+[[5,6,7]] => A [1,2,3,[5,6,7]] - add lists
# A.append([5,6,7])
# A.insert(2, 100) => A [1,2,100,3] insert element in a specific place in the list
