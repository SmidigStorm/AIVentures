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
        character.hit_points = min(character.max_hit_points, character.hit_points + self.healing_amount)
        print(f"{character.name} used {self.name} and healed for {self.healing_amount} hit points!")