#BabySimulator
#choice from the list
from random import choice
questions = ["Why? ", "Are you sure? ", "How? "]
answer= input("How are you?").strip().lower()
while answer !="just because":
    question = choice(questions)
    answer=input(question).strip().lower()
print ("Oh..okay")
