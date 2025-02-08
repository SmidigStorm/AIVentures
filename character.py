from entity import Entity

class Character(Entity):
    def __init__(self, name, race, class_name, strength, dexterity, constitution, intelligence, wisdom, charisma,
                 hit_points, armor_class, damage_reduction):
        super().__init__(name, race, class_name, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.max_hit_points = hit_points
        self.current_hit_points = hit_points
        self.armor_class = armor_class
        self.damage_reduction = damage_reduction
        self.inventory = []
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = self.calculate_xp_to_next_level()


    def assign_stats(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma


    def add_skill(self, skill, proficiency):
        self.skills[skill] = proficiency

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def use_item(self, item):
        if item in self.inventory:
            item.use(self)
            self.remove_item(item)
            return True
        return False

    def get_usable_items(self):
        return [item for item in self.inventory if item.is_usable_in_battle]

    def calculate_xp_to_next_level(self):
        return self.level * 1000  # Simple calculation, can be adjusted for balance

    def gain_xp(self, xp):
        self.xp += xp
        print(f"{self.name} gained {xp} XP!")
        while self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_next_level
        self.xp_to_next_level = self.calculate_xp_to_next_level()

        # Increase stats
        self.strength += Dice.roll_d4()
        self.dexterity += Dice.roll_d4()
        self.constitution += Dice.roll_d4()
        self.intelligence += Dice.roll_d4()
        self.wisdom += Dice.roll_d4()
        self.charisma += Dice.roll_d4()

        # Increase hit points
        hit_points_increase = Dice.roll_d8() + self.get_constitution_modifier()
        self.max_hit_points += hit_points_increase
        self.current_hit_points += hit_points_increase

        print(f"{self.name} has leveled up to level {self.level}!")
        print(f"Hit Points increased by {hit_points_increase}")
        print("All attributes have increased!")

    def get_constitution_modifier(self):
        return (self.constitution - 10) // 2

    def get_stats(self):
        stats = super().get_stats()
        stats += f"Level: {self.level}\n"
        stats += f"XP: {self.xp}/{self.xp_to_next_level}\n"
        stats += f"Current Hit Points: {self.current_hit_points}/{self.max_hit_points}\n"
        return stats

    def heal(self, amount):
        self.current_hit_points = min(self.max_hit_points, self.current_hit_points + amount)
        return amount

    def take_damage(self, amount):
        self.current_hit_points = max(0, self.current_hit_points - amount)
        return amount

    def is_alive(self):
        return self.current_hit_points > 0
