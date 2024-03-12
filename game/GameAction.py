from typing import List

from characters.Npc import Npc
from error.OutOfManaException import OutOfManaException
from game.GamePrinter import GamePrinter
from game.GameRandom import GameRandom
from spells.Spell import Spell


class GameAction:
    __heroes: List[Npc]
    __monsters: List[Npc]

    def __init__(self, heroes: List[Npc], monsters: List[Npc]):
        self.__heroes = heroes
        self.__monsters = monsters

    def heroes_action(self):
        self.__group_action(self.__heroes, self.__monsters)

    def monsters_action(self):
        self.__group_action(self.__monsters, self.__heroes)

    def __group_action(self, attacker_group: List[Npc], target_group: List[Npc]):
        for attacker in attacker_group:
            self.__attack_action(attacker, target_group)

    def __attack_action(self, attacker: Npc, target_group: List[Npc]):
        target: Npc = GameRandom.random_target_from_list(target_group)

        self.__decide_attacker_action(attacker, target)
        self.__update_target_group_status(target, target_group)

    def __decide_attacker_action(self, attacker: Npc, target: Npc):
        if GameRandom.is_attacker_using_spell(attacker):
            self.__use_spell(attacker, target)
        else:
            self.__normal_attack(attacker, target)

    def __use_spell(self, attacker: Npc, target: Npc):
        spell: Spell = GameRandom.random_spell_by(attacker)
        try:
            magic_damage:int = attacker.use_spell(spell, target)
            GamePrinter.spell_used_text(spell, attacker, target)
            GamePrinter.damage_text(target, magic_damage)
        except OutOfManaException:
            GamePrinter.out_of_mana_text(spell, attacker)

    def __normal_attack(self, attacker: Npc, target: Npc):
        damage: int = attacker.attack(target)

        GamePrinter.attack_text(attacker, target)
        GamePrinter.damage_text(target, damage)

    def __update_target_group_status(self, target_attacked: Npc, target_group: List[Npc]):
        if target_attacked.alive is False:
            self.__defeat_target(target_attacked, target_group)
        self.__check_if_groups_are_alive()

    def __defeat_target(self, target_defeated: Npc, target_group: List[Npc]):
        GamePrinter.defeated_text(target_defeated)
        target_group.remove(target_defeated)

    def __check_if_groups_are_alive(self):
        if not self.__heroes:
            self.__end_battle("Monsters")
        elif not self.__monsters:
            self.__end_battle("Heroes")

    def __end_battle(self, winner_group: str):
        GamePrinter.vertical_space()
        GamePrinter.end_of_battle_text(winner_group)
        exit(0)
