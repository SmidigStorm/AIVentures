import json
from character import Character


class CharacterFactory:
    def __init__(self):
        with open("races.json") as f:
            self.races = json.load(f)

        with open("races_default_values.json") as default_values_file:
            self.races_defaults = json.load(default_values_file)

    def create_character(self, name, race, class_name, strength, dexterity, constitution, intelligence, wisdom,
                         charisma):
        race_stats = self.races[race]
        race_default_values = self.races_defaults[race]

        char = Character()

        character = char.Character(name, race, class_name, race_default_values["strength"] + race_stats["strength_bonus"],
                              race_default_values["dexterity"] + race_stats["dexterity_bonus"],
                              race_default_values["constitution"] + race_stats["constitution_bonus"],
                              race_default_values["intelligence"] + race_stats["intelligence_bonus"],
                              race_default_values["wisdom"] + race_stats["wisdom_bonus"],
                              race_default_values["charisma"] + race_stats["charisma_bonus"])
        return character

# 1d6: 4 rolls remove lowest, choose BEST one. Instead of default
# Start on 8 on all stats, then use allocation points
# 15, 14, 13, 12, 10, 8 as default values, then add race and then class.

# RACE -> CLASS -> Character
# Equipment -> Weapon -> Dagger
# Equipment -> Armour ->