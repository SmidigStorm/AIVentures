from GameState import GameState
from battleAI import Battle
from characterFactory import CharacterFactory
from monsterFactory import MonsterFactory
from charactercreator import CharacterCreator

def main():
    # Create character using CharacterCreator
    creator = CharacterCreator()
    player_character = creator.create_character()

    # Initial setup state
    gamestate = GameState(player_character, MonsterFactory)
    battle = Battle(gamestate.character, gamestate.monster)

    # Main loop
    while True:
        print("\n---- Current State ----")
        print(gamestate.character.get_stats())
        print(gamestate.monster.get_stats())

        # Get user input
        command = input("\nWhat would you like to do? (a)ttack or (q)uit: ")

        # Process input
        if command.lower() == "a":
            winner = battle.run_battle()
            if winner == "player":
                battle.end_battle(winner == "player")
                gamestate.monster_kills += 1
            elif winner == "monster":
                print("You have lost the battle...")
                return
        elif command.lower() == "q":
            print("Goodbye!")
            return
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()