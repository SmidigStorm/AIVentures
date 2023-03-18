from battle import Battle
from characterFactory import CharacterFactory
from dice import Dice
from monsterFactory import MonsterFactory

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# CHARACTER #
character_factory = CharacterFactory()

print("---- BEFORE BATTLE ----")
character = character_factory.create_character("Lazarus", "Elf", "ranger")
print(character.get_stats())

# MONSTER #
monster_factory = MonsterFactory()

monster = monster_factory.create_monster("Baltazar", "Goblin", "ranger")
print(monster.get_stats())


# ROLL #
#d4_roll = Dice.roll_d4()
# Input to roll method should be 4, 6, 8, 20
#print(f"1D4 Roll: {d4_roll}")
#print(f"1D6 Roll: {Dice.roll_d6()}")

# BATTLE #
battle = Battle(character, monster)


initiative_list = battle.calculate_initiative() # Who goes first
for item in initiative_list:
    print(f"{item[0]} has an initiative roll of {item[1]}")

winner = battle.run_battle()
battle.end_battle(winner == "player")
print("---- AFTER BATTLE ----")
print(character.get_stats())
print(monster.get_stats())