from character import Character

class Battle:
    """Manages turn-based combat between two characters."""

    def __init__(self, hero: Character, enemy: Character):
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        if not (self.hero.is_alive and self.enemy.is_alive):
            return
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self, max_rounds: int = 1000) -> None:
        """Run combat, raising RuntimeError if the round limit is reached.

        A limit prevents endless combat when armor blocks all damage. A single
        round without damage is allowed because later dice rolls or mana
        regeneration can still change the outcome.
        """
        if max_rounds < 1:
            raise ValueError("Maximum rounds must be at least 1.")
        rounds = 0
        while self.hero.is_alive and self.enemy.is_alive:
            if rounds >= max_rounds:
                raise RuntimeError("The battle has lasted eons! Return home champions.")
            self.play_round()
            rounds += 1
            print(f"{self.hero.name} HP: {self.hero.hp}, {self.enemy.name} HP: {self.enemy.hp}")
        if not self.hero.is_alive:
            print(f"{self.hero.name} has been defeated by {self.enemy.name}. BUMMER!")
        elif not self.enemy.is_alive:
            print(f"{self.enemy.name} has been defeated by {self.hero.name}. YIPPEE!")
