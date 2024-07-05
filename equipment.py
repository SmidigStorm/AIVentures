
class Equipment:
    def __init__(self, name, equipment_type, stat_bonuses):
        self.name = name
        self.equipment_type = equipment_type
        self.stat_bonuses = stat_bonuses

    def __str__(self):
        return f"{self.name} ({self.equipment_type}) - {self.stat_bonuses}"

    def apply_bonuses(self, character):
        for stat, bonus in self.stat_bonuses.items():
            setattr(character, stat, getattr(character, stat) + bonus)

    def remove_bonuses(self, character):
        for stat, bonus in self.stat_bonuses.items():
            setattr(character, stat, getattr(character, stat) - bonus)
