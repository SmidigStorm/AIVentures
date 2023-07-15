from battle import Battle
from characterFactory import CharacterFactory
from dice import Dice
from monsterFactory import MonsterFactory

# CHARACTER #
character_factory = CharacterFactory()

print("---- BEFORE BATTLE ----")
character = character_factory.create_character("Lazarus", "Elf", "Ranger")
print(character.get_stats())

# MONSTER #
monster_factory = MonsterFactory()

monster = monster_factory.create_monster("Baltazar", "Goblin", "Ranger")
print(monster.get_stats())


# BATTLE #
battle = Battle(character, monster)

initiative_list = battle.calculate_initiative()  # Who goes first
for item in initiative_list:
    print(f"{item[0]} has an initiative roll of {item[1]}")

winner = battle.run_battle()  # FIGHT
battle.end_battle(winner == "player")  # Only give out xp and levels to player if they won
print("---- AFTER BATTLE ----")
print(character.get_stats())
print(monster.get_stats())