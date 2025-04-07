import json
from weapon import Weapon


class WeaponFactory:
    def __init__(self):
        with open("weapon-catalog.json") as f:
            self.weapon_catalog = json.load(f)

        # Combine all weapons into a single dictionary for easy access
        self.all_weapons = {}
        for category, weapons in self.weapon_catalog.items():
            for weapon_name, weapon_data in weapons.items():
                self.all_weapons[weapon_name] = weapon_data
                # Add the weapon type (simple_melee, martial_ranged, etc.) to the data
                self.all_weapons[weapon_name]["type"] = category

    def get_weapon_list(self):
        """Returns a list of all weapon names."""
        return list(self.all_weapons.keys())

    def get_weapon_by_name(self, weapon_name):
        """Creates and returns a Weapon object based on the weapon name."""
        if weapon_name not in self.all_weapons:
            raise ValueError(f"Weapon {weapon_name} not found in the catalog")

        weapon_data = self.all_weapons[weapon_name]
        properties = weapon_data.get("properties", [])
        damage_dice_count = weapon_data.get("damage_dice_count", 1)

        return Weapon(
            name=weapon_name,
            damage_die=weapon_data["damage_die"],
            damage_type=weapon_data["damage_type"],
            category=weapon_data["category"],
            properties=properties,
            damage_dice_count=damage_dice_count
        )