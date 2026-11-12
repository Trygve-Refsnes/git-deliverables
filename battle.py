from character import Character
from character import Warrior
from character import Mage

class Battle:
    """Manages turn-based combat between two characters."""

    def __init__(self, hero: Character, enemy: Character):
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        hero_damage = self.hero.damage
        self.enemy.take_damage(hero_damage)
        if self.enemy.is_alive:
            enemy_damage = self.enemy.damage
            self.hero.take_damage(enemy_damage)

    def simulate_battle(self) -> None:
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()