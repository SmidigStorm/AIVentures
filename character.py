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

    def level_up(self):
        self.level += 1

    def gain_xp(self, xp):
        self.xp += xp

    def heal(self, amount):
        self.current_hit_points = min(self.max_hit_points, self.current_hit_points + amount)
        return amount

    def take_damage(self, amount):
        actual_damage = max(0, amount - self.damage_reduction)
        self.current_hit_points = max(0, self.current_hit_points - actual_damage)
        return actual_damage

    def is_alive(self):
        return self.current_hit_points > 0

    def get_stats(self):
        stats = super().get_stats()
        stats += f"Current Hit Points: {self.current_hit_points}/{self.max_hit_points}\n"
        return stats