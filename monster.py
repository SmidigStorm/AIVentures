class Monster:
    # This is a copy of the character class,
    # TODO: Needs to be refactored with inheritance together with the character class.

    # You can then use this class to create new characters and set their properties.
    #
    # You can use the roll_stats() method to randomly assign the statistics
    # , assign_stats() method to set the statistics manually
    # , the add_skill() method to add skills and proficiency to the character
    # , the add_item() method to add an item to the inventory
    # , the level_up() method to increase the character's level
    # , the gain_xp() method to increase the character's XP
    # , and the display_stats() method to display the character's information.
    class Monster:
        def __init__(self, name, race, class_name, strength, dexterity, constitution, intelligence, wisdom, charisma):
            self.name = name
            self.race = race
            self.class_name = class_name
            self.strength = strength
            self.dexterity = dexterity
            self.constitution = constitution
            self.intelligence = intelligence
            self.wisdom = wisdom
            self.charisma = charisma

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
# this method needs moving or changed to a get stats..
    def display_stats(self):
        print("Name:", self.name)
        print("Race:", self.race)
        print("Class:", self.char_class)
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
