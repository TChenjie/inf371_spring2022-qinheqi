import random
class Character:
     def __init__(self,strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength=strength
        self.dexterity=dexterity
        self.constitution=constitution
        self.intelligence=intelligence
        self.wisdom=wisdom
        self.charisma=charisma
        self.hitpoints=constitution*30+50
     def printststs(self):
        print_stats=f"player stats are {self.strength},{self.dexterity},{self.constitution},{self.intelligence},{self.wisdom},{self.charisma}"
        return print_stats
     def hitpoints1(self):
        print_hitpoints=f"hitpoint is {self.hitpoints}"
        return print_hitpoints