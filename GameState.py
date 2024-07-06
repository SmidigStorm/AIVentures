from items import HealingPotion
class GameState:
    def __init__(self, CharacterFactory, MonsterFactory):
        # Setup: Create character, monster, and initial equipment
        character_factory = CharacterFactory()
        monster_factory = MonsterFactory()
        self.monster_kills = 0

        self.character = character_factory.create_character("Lazarus", "Elf", "ranger")
        self.monster = monster_factory.create_monster("Baltazar", "Goblin", "ranger")

        # Add initial items to the character's inventory
        self.character.add_item(HealingPotion("Small Healing Potion", 10))
        self.character.add_item(HealingPotion("Medium Healing Potion", 25))

