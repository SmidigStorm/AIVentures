from entity import Entity

class Character(Entity):
    def __init__(self, name, race, class_name, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(name, race, class_name, strength, dexterity, constitution, intelligence, wisdom, charisma)

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

    def get_stats(self):
        stats = (
            f"Name: {self.name}\n"
            f"Race: {self.race}\n"
            f"Class: {self.class_name}\n"
            f"Strength: {self.strength}\n"
            f"Dexterity: {self.dexterity}\n"
            f"Constitution: {self.constitution}\n"
            f"Intelligence: {self.intelligence}\n"
            f"Wisdom: {self.wisdom}\n"
            f"Charisma: {self.charisma}\n"
            f"Skills: {self.skills}\n"
            f"Inventory: {self.inventory}\n"
            f"Level: {self.level}\n"
            f"Experience Points: {self.xp}"
        )
        return stats
