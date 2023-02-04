import json
from monster import Monster


class MonsterFactory:
    def __init__(self):
        with open("monster_default_values.json") as f:
            self.races = json.load(f)

    def create_monster(self, name, race, class_name, strength, dexterity, constitution, intelligence, wisdom,
                       charisma):
        race_stats = self.races[race]
        monster = Monster()

        character = monster.Monster(name, race, class_name, strength, dexterity,
                              constitution,
                              intelligence,
                              wisdom, charisma)
        return character
