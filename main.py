from GameState import GameState
from battleAI import Battle
from characterFactory import CharacterFactory
from monsterFactory import MonsterFactory
from charactercreator import CharacterCreator

def main():
    creator = CharacterCreator()
    player = creator.create_character()
    gamestate = GameState(player, MonsterFactory)

    # Main loop
    playing = True # TODO: Add more states later (CREATOR, IDLE, BATTLE, ENDING
    while playing:
        print("\n---- Current State ----")

        gamestate.monster.level = gamestate.character.level

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
                # Creating a new monster for next round
                monster = MonsterFactory().create_monster("Baltazar2", "Goblin","Ranger",2)
                gamestate.monster = monster
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