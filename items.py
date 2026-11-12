from dice import Dice

class Weapon:
    def __init__(self, name: str, damage_dice: Dice):
        """Initialise the Weapon"""
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the damage dice to determine the damage dealt by the weapon."""
        return self.damage_dice.roll()