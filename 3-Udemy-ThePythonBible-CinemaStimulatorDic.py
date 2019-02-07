#Dictionaries
# students= {
#     "Alice":{"id":"ID001", "age":26, "grade":"A"},
#     "bob":{"id":"ID002", "age":27, "grade":"B"},
#     "Claire":{"id":"ID003", "age":17, "grade":"C"},
#     "Dan":{"id":"ID004", "age":21, "grade":"D"},
#     "Emma":{"id":"ID005", "age":22, "grade":"E"}
# }

# print (students["Alice"]["age"])
# print (students["Emma"]["id"], students["Emma"]["age"])

# Create a cinema stimulator
films ={
    "Finding Dory": [3,2],
    "Bourne":[18,5],
    "Tarzan":[15,1],
    "Ghost Busters":[12,5]
}

while True:
   choice= input("What film would you like to watch:").strip().title()
   if choice in films:
        age = int(input("How old are you?:").strip())
       # check user age
        if age >= films[choice][0]:
            # check enough seats
            if films[choice][1]>0:
                print ("Enjoy the film")
                print ("Total available seats: {}".format(films[choice][1]))
                films[choice][1]=films[choice][1]-1
            else:
             print("Sorry,no sits")

        else:
            print("You are too young")
   else:
       print("We don't have that film...")
