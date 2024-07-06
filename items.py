class Item:
    def __init__(self, name, description, is_usable_in_battle=True):
        self.name = name
        self.description = description
        self.is_usable_in_battle = is_usable_in_battle

    def use(self, character):
        raise NotImplementedError("This method should be implemented by subclasses")

class HealingPotion(Item):
    def __init__(self, name, healing_amount):
        super().__init__(name, f"Heals {healing_amount} hit points")
        self.healing_amount = healing_amount

    def use(self, character):
        healed_amount = character.heal(self.healing_amount)
        print(f"{character.name} used {self.name} and healed for {healed_amount} hit points!")
        print(f"Current HP: {character.current_hit_points}/{character.max_hit_points}")