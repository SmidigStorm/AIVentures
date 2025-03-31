from GameState import GameState
from battleAI import Battle
from characterFactory import CharacterFactory
from monsterFactory import MonsterFactory
from charactercreator import CharacterCreator

def main():
    # Create character using CharacterCreator
    creator = CharacterCreator()
    player_character = creator.create_character()


    # Main loop
    playing = True
    while playing:
        print("\n---- Current State ----")
        gamestate = GameState(player_character, MonsterFactory)
        print(gamestate.character.get_stats())
        print(gamestate.monster.get_stats())

        # Get user input
        command = input("\nWhat would you like to do? (a)ttack or (q)uit: ")

        # Process input
        if command.lower() == "a":
            battle = Battle(gamestate.character, gamestate.monster)
            winner = battle.run_battle()

            if winner == "player":
                print(f"Victory! You defeated {gamestate.monster.name}!")
                gamestate.monster_kills += 1
                playing = True
            elif winner == "monster":
                print(f"Game Over! {gamestate.character.name} has been defeated...")
                playing = False
        elif command.lower() == "q":
            print("Goodbye!")
            playing = False
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()