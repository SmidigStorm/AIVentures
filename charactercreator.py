import json
from characterFactory import CharacterFactory


class CharacterCreator:
    def __init__(self):
        self.character_factory = CharacterFactory()

        with open("races.json") as jsonfile:
            self.races = json.load(jsonfile)

        with open("classes.json") as jsonfile:
            self.classes = json.load(jsonfile)

    def create_character(self):
        name = self.get_character_name()
        race = self.choose_race()
        class_name = self.choose_class()

        character = self.character_factory.create_character(name, race, class_name)
        return character

    def get_character_name(self):
        while True:
            name = input("Enter your character's name: ").strip()
            if name:
                return name
            print("Name cannot be empty. Please try again.")

    def choose_race(self):
        print("\nAvailable races:")
        for i, race in enumerate(self.races.keys(), 1):
            print(f"{i}. {race}")

        while True:
            choice = input("Choose a race (enter the number): ")
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.races):
                    return list(self.races.keys())[index]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def choose_class(self):
        print("\nAvailable classes:")
        for i, class_name in enumerate(self.classes, 1):
            print(f"{i}. {class_name}")

        while True:
            choice = input("Choose a class (enter the number): ")
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.classes):
                    return self.classes[index]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")


##def main():
##    creator = CharacterCreator()
##    character = creator.create_character()
##    print("\nCharacter created successfully!")
##    print(character.get_stats())


##if __name__ == "__main__":
##    main()