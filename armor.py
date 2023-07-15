from equipment import Equipment
from equipmentType import EquipmentType


class Armor(Equipment):
    def __init__(self, name: str, ac_bonus: int, equipment_type: EquipmentType):
        super().__init__(name, equipment_type)
        self.ac_bonus = ac_bonus

    def get_ac_bonus(self):
        return self.ac_bonus
