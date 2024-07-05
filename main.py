from GameState import GameState
from battleAI import Battle
from characterFactory import CharacterFactory
from monsterFactory import MonsterFactory


def main():
    # Initial setup state
    gamestate = GameState(CharacterFactory, MonsterFactory)
    battle = Battle(gamestate.character, gamestate.monster)


    # Main loop
    while True:
        print("\n---- Current State ----")
        print(gamestate.character.get_stats())
        print(gamestate.monster.get_stats())

        # Get user input
        command = input("\nWhat would you like to do? (attack/quit): ")

        # Process input
        if command.lower() == "attack":
            winner = battle.run_battle()
            if winner == "player":
                print("You have won the battle!")
                battle.end_battle(winner == "player")
                gamestate.monster_kills += 1
                print(gamestate.monster_kills)
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
