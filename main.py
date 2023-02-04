from characterFactory import CharacterFactory
from dice import Dice
from monsterFactory import MonsterFactory

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# CHARACTER #
character_factory = CharacterFactory()

# character = factory.create_character("John", "human","warrior", 10, 10 , 10 , 10, 10, 10)
character = character_factory.create_character("Lazarus", "Elf", "ranger", 10, 10, 10, 10, 10, 10)
print("Name:" + character.name)
print("Race:" + character.race)
print("Class:" + character.class_name)
print("Str:", character.strength)
print("Dex:", character.dexterity)
print("Int:", character.intelligence)
print("Wis:", character.wisdom)
print("Cha:", character.charisma)


# MONSTER #
monster_factory = MonsterFactory()

monster = monster_factory.create_monster("Subbegutt", "Goblin", "ranger", 10, 10, 10, 10, 10, 10)
print("Name:" + monster.name)
print("Race:" + monster.race)
print("Class:" + monster.class_name)
print("Str:", monster.strength)
print("Dex:", monster.dexterity)
print("Int:", monster.intelligence)
print("Wis:", monster.wisdom)
print("Cha:", monster.charisma)


# ROLL #
d4_roll = Dice.roll_d4()
# Input to roll method should be 4, 6, 8, 20
print(f"1D4 Roll: {d4_roll}")
print(f"1D6 Roll: {Dice.roll_d6()}")