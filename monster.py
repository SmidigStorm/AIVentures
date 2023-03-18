from entity import Entity

class Monster(Entity):
    def __init__(self, name, race, class_name, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(name, race, class_name, strength, dexterity, constitution, intelligence, wisdom, charisma)

    def roll_stats(self):
        # Code to roll for stats
        pass

    def assign_stats(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def add_skill(self, skill, proficiency):
        self.skills[skill] = proficiency

    def add_item(self, item):
        self.inventory.append(item)

    def level_up(self):
        self.level += 1

    def gain_xp(self, xp):
        self.xp += xp

    def display_stats(self):
        print("Name:", self.name)
        print("Race:", self.race)
        print("Class:", self.class_name)
        print("Strength:", self.strength)
        print("Dexterity:", self.dexterity)
        print("Constitution:", self.constitution)
        print("Intelligence:", self.intelligence)
        print("Wisdom:", self.wisdom)
        print("Charisma:", self.charisma)
        print("Skills:", self.skills)
        print("Inventory:", self.inventory)
        print("Level:", self.level)
        print("Experience Points:", self.xp)
