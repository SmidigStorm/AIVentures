from character import Character
from monster import Monster
from dice import Dice
class Battle:
    # Simple implementation of a battle between player and monster
    # meant to be used by a battle generator class
    # I could also see it having battle helper classes also for specific calculations or similar

    def __init__(self, character, monster):
        self.character = character
        self.monster = monster

    def calculate_initiative(self):
        initiative = []
        initiative.append((self.character.name, self.character.dexterity + Dice.roll_d20()))
        initiative.append((self.monster.name, self.monster.dexterity + Dice.roll_d20()))
        initiative.sort(key=lambda x: x[1], reverse=True)
        return initiative

