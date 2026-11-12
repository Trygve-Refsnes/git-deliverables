from items import Weapon

class Character:
    """Represents a character in the RPG"""
    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None
        ) -> None:
        """
        Initialise the Character
        Args:
        name (str): The name of the character.
        hp_max (int): Max hit points (default = 100)
        damage (int): Damage dealt when character attacks (default = 10)
        weapon (Weapon, optional): The weapon the character wields (default = None)
        """
        self.name = name
        self._hp = hp_max # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def attack(self, target) -> None:
        """Attack a target using weapon damage if equipped, otherwise base damage."""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage
        target.take_damage(damage)


    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")


    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    
    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"
    
    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe
        edits."""
        return self._hp 

    def take_damage(self, amount: int) -> None:
        """Reduces the character's HP by the specified amount of damage."""
        self._hp -= amount
        self._hp = min(self._hp, self.hp_max)  # Ensure HP does not exceed max HP
        self._hp = max(self._hp, 0)  # Ensure HP does not go below 0

    def heal(self, amount: int) -> None:
        """Increases the character's HP by the specified amount, up to the maximum HP."""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)  # Ensure HP does not exceed max HP
        self._hp = max(self._hp, 0) # Ensure HP does not go below 0

    @property
    def is_alive(self) -> bool:
        """Returns True if the character is alive (HP > 0), otherwise False."""
        return self._hp > 0
    

class Warrior(Character):
    """Represents a warrior character in the RPG"""


    def __init__(self, name: str, armor: int = 5, **kwargs):
        super().__init__(name, **kwargs)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        # Calculate damage after armor reduction
        damage_after_armor = max(0, amount - self.armor)
        super().take_damage(damage_after_armor)

class Mage(Character):
    """Represents a mage character in the RPG"""

        
    def __init__(self, name: str, mana: int = 30, mana_max: int = 30, **kwargs):
        super().__init__(name, **kwargs)
        self.mana = mana
        self.mana_max = mana_max
        self.mana_max = max(self.mana_max, 0)  # Ensure max mana is not negative
        self.mana = min(self.mana, self.mana_max)  # Ensure mana does not exceed max mana
        self.mana = max(self.mana, 0)  # Ensure mana does not go below 0

    def attack(self, target) -> None:
        """Attack a target using magic if enough mana is available, otherwise base damage."""
        if self.mana >= 10:
            damage = self.damage * 2  # Magic attack deals double damage
            self.mana -= 10  # Consume mana for magic attack
            target.take_damage(damage)
        else:
            super().attack(target)
            self.mana += 5
            self.mana = min(self.mana, self.mana_max)