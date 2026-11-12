from character import Character

class Battle:
    """Manages turn-based combat between two characters."""

    def __init__(self, hero: Character, enemy: Character):
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()
            print(f"{self.hero.name} HP: {self.hero.hp}, {self.enemy.name} HP: {self.enemy.hp}")
        if not self.hero.is_alive:
            print(f"{self.hero.name} has been defeated by {self.enemy.name}. BUMMER!")
        elif not self.enemy.is_alive:
            print(f"{self.enemy.name} has been defeated by {self.hero.name}. YIPPEE!")