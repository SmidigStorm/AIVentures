import unittest
from dice import Dice
# This is more a test of making a unittest. Testing randomint does not really make any sense...
class TestDice(unittest.TestCase):
    def test_roll_d4(self):
        # Arrange
        dice = Dice()

        # Act
        result = dice.roll_d4()

        # Assert
        self.assertTrue(1 <= result <= 4)

    def test_roll_d6(self):
        # Arrange
        dice = Dice()

        # Act
        result = dice.roll_d6()

        # Assert
        self.assertTrue(1 <= result <= 6)

    def test_roll_d8(self):
        # Arrange
        dice = Dice()

        # Act
        result = dice.roll_d8()

        # Assert
        self.assertTrue(1 <= result <= 8)

    def test_roll_d20(self):
        # Arrange
        dice = Dice()

        # Act
        result = dice.roll_d20()

        # Assert
        self.assertTrue(1 <= result <= 20)

if __name__ == '__main__':
    unittest.main()
