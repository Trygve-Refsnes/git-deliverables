import random

class Dice:
    """A class representing a dice with a specified number of sides."""


    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the Dice
        Args:
        sides (int): The number of sides on the dice (default = 6)
        """
        if sides > 2:
            self.sides = sides
        else:
            raise ValueError("Dice must have more than 2 sides.")
        

    def roll(self) -> int:
        """Roll the dice and return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)


    def __repr__(self) -> str:
        """Representation of dice object"""
        return f"<Dice sides={self.sides}>"
    

    def __call__(self):
        return self.roll()

