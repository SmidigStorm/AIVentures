from battle import Battle
from characterFactory import CharacterFactory
from dice import Dice
from monsterFactory import MonsterFactory


def main():
    # Setup: Create character, monster, and initial equipment
    character_factory = CharacterFactory()
    monster_factory = MonsterFactory()

    character = character_factory.create_character("Lazarus", "Elf", "ranger")
    monster = monster_factory.create_monster("Baltazar", "Goblin", "ranger")

    battle = Battle(character, monster)

    # Main loop
    while True:
        print("\n---- Current State ----")
        print(character.get_stats())
        print(monster.get_stats())

        # Get user input
        command = input("\nWhat would you like to do? ")

        # Process input
        if command.lower() == "attack":
            winner = battle.run_battle()
            if winner == "player":
                print("You have won the battle!")
                battle.end_battle(winner == "player")
            elif winner == "monster":
                print("You have lost the battle...")
                return
        elif command.lower() == "quit":
            print("Goodbye!")
            return
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
