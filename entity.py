from armor import Armor
from equipmentType import EquipmentType
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
        self.equipment = {eq_type: None for eq_type in EquipmentType}

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

    def equip(self, item):
        if item.equipment_type in self.equipment:
            self.unequip(item.equipment_type)
            self.equipment[item.equipment_type] = item
            self.update_stats(item, equip=True)
            print(f"{self.name} has equipped {item.name}.")

    def unequip(self, equipment_type):
        item = self.equipment[equipment_type]
        if item:
            self.update_stats(item, equip=False)
            self.equipment[equipment_type] = None
            print(f"{self.name} has unequipped {item.name}.")

    def update_stats(self, item, equip=True):
        factor = 1 if equip else -1
        self.strength += factor * item.strength
        self.dexterity += factor * item.dexterity
        self.constitution += factor * item.constitution
        self.intelligence += factor * item.intelligence
        self.wisdom += factor * item.wisdom
        self.charisma += factor * item.charisma

    def calculate_armor_class(self):
        ac = 10  # Start with base armor class (AC)
        for equipment in self.equipment.values():
            if isinstance(equipment, Armor):
                ac += equipment.get_ac_bonus()
        return ac
