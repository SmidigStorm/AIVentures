import random

class Dice:
    @staticmethod
    def roll(dice_type: int) -> int:
        return random.randint(1, dice_type)

    @staticmethod
    def roll_d4() -> int:
        return Dice.roll(4)

    @staticmethod
    def roll_d6() -> int:
        return Dice.roll(6)

    @staticmethod
    def roll_d8() -> int:
        return Dice.roll(8)

    @staticmethod
    def roll_d10() -> int:
        return Dice.roll(10)

    @staticmethod
    def roll_d12() -> int:
        return Dice.roll(12)

    @staticmethod
    def roll_d20() -> int:
        return Dice.roll(20)

    @staticmethod
    def roll_d100() -> int:
        return Dice.roll(100)
