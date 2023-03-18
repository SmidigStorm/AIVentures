class Entity:
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
        self.skills = {}
        self.inventory = []
        self.level = 1
        self.xp = 0
        XP_TABLE = [0, 100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500]  # Example XP table

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
        while self.level < len(self.XP_TABLE) and self.xp >= self.XP_TABLE[self.level]:
            self.level_up()
