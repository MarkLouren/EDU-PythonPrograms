#classes coins.py [Methods]
import random
class Pound:
    def __init__(self, rare=False):
        self.rare = rare
        # the dame self.rare=True=>
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00

        self.value = 1.00
        self.colour = "gold"
        self. num_edges = 1
        self.diameter = 22.5  # mm
        self.thickness = 3.15  # mm
        self.heads = True
    # create a method example: coin1.rust() => coin1.colour=> greenish
    def rust(self):
        self.colour="greenish"
    def clear (self):
        self.colour="gold"
    #flip coin => coin1.flip() => True or False
    def flip(self):
        heads_options =[True, False]
        choice = random.choice(heads_options)
        self.heads=choice
    #destructor method => del coin1 => Coin Spent=>not defined
    def __del__(self):
        print ("Coin Spent")
