import contextlib
import io
import unittest

from battle import Battle
from character import Character, Mage, Warrior
from dice import Dice
from items import Weapon


class FixedDice(Dice):
    def roll(self):
        return 7


class GameTests(unittest.TestCase):
    def test_health_bounds_and_read_only_properties(self):
        with self.assertRaises(ValueError):
            Character("Invalid", hp_max=-1)
        character = Character("Hero", hp_max=20)
        character.take_damage(100)
        self.assertEqual(character.hp, 0)
        self.assertFalse(character.is_alive)
        character.heal(100)
        self.assertEqual(character.hp, 20)
        for attribute in ("hp", "is_alive"):
            with self.assertRaises(AttributeError):
                setattr(character, attribute, 0)

    def test_mage_ignores_weapon_for_spell_and_uses_it_for_fallback(self):
        mage = Mage("Mage", mana=10, weapon=Weapon("Staff", FixedDice(8)))
        target = Character("Target")
        mage.attack(target)
        self.assertEqual((target.hp, mage.mana), (80, 0))
        mage.attack(target)
        self.assertEqual((target.hp, mage.mana), (73, 5))

    def test_armor_and_finished_round(self):
        warrior = Warrior("Warrior")
        warrior.take_damage(3)
        self.assertEqual(warrior.hp, 100)
        warrior.take_damage(12)
        self.assertEqual(warrior.hp, 93)
        hero = Character("Hero", hp_max=10, damage=10)
        enemy = Character("Enemy", hp_max=10)
        battle = Battle(hero, enemy)
        battle.play_round()
        self.assertEqual((hero.hp, enemy.hp), (10, 0))
        battle.play_round()
        self.assertEqual((hero.hp, enemy.hp), (10, 0))

    def test_blocked_battle_terminates_at_limit(self):
        battle = Battle(Warrior("A", damage=5), Warrior("B", damage=5))
        with contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(RuntimeError):
                battle.simulate_battle(max_rounds=3)
        self.assertEqual((battle.hero.hp, battle.enemy.hp), (100, 100))
        with self.assertRaises(ValueError):
            battle.simulate_battle(max_rounds=0)

    def test_no_damage_round_can_be_followed_by_mage_spell(self):
        hero = Mage("Mage", mana=5, damage=4, hp_max=30)
        enemy = Warrior("Warrior", hp_max=3, damage=0)
        with contextlib.redirect_stdout(io.StringIO()):
            Battle(hero, enemy).simulate_battle(max_rounds=2)
        self.assertTrue(hero.is_alive)
        self.assertFalse(enemy.is_alive)


if __name__ == "__main__":
    unittest.main()
