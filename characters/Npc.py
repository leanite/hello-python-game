from abc import ABC
from typing import List

from error.OutOfManaException import OutOfManaException
from etc.DamageType import DamageType
from etc.Number import Number
from items import Weapon
from spells import Spell
from spells.SpellCaster import SpellCaster


class Npc(SpellCaster, ABC):
    name: str
    character_class: str
    alive: bool
    hp: int
    mana: int
    attack_power: int
    attack_modifier: float
    magic_power: int
    defense: int
    defense_modifier: float
    magic_defense: int
    magic_defense_modifier: float
    weapon: Weapon = None
    spells: List[Spell]

    #  target: 'Npc' é uma dica para o Python de que o tipo Npc será definido mais tarde.
    #  Isso resolverá o erro de referência não reconhecida ao nome Npc em target: Npc
    def attack(self, target: 'Npc') -> int:
        return target.__take_damage(self.__calculate_attack_damage(), DamageType.PHYSICAL)

    def use_spell(self, spell: Spell, target: 'Npc') -> int:
        if self.__can_use_spell(spell):
            self.mana -= spell.mana_cost
        else:
            raise OutOfManaException()

        return target.__take_damage(spell.calculate_spell_damage(self), DamageType.MAGIC)

    def __can_use_spell(self, spell: Spell) -> bool:
        return self.mana >= spell.mana_cost

    def __calculate_attack_damage(self) -> int:
        return self.__get_base_damage() + self.__generate_random_attack_damage()

    def __get_base_damage(self) -> int:
        return Number.round(self.attack_power * self.attack_modifier)

    def __generate_random_attack_damage(self) -> int:
        weapon_random_damage: int = 0

        if self.has_weapon():
            weapon_random_damage = Number.random_with_lower_one(self.weapon.attack_power)

        return weapon_random_damage

    def __take_damage(self, damage: int, damage_type: DamageType) -> int:
        damage_taken: int = self.__calculate_damage_taken(damage, damage_type)

        self.__lose_hit_points(damage_taken)
        self.__check_alive_status()

        return damage_taken

    def __calculate_damage_taken(self, damage: int, damage_type: DamageType) -> int:
        true_damage: int = self.__calculate_true_damage_by_damage_type(damage, damage_type)

        return self.__check_negative_damage(true_damage)

    def __calculate_true_damage_by_damage_type(self, damage: int, damage_type: DamageType) -> int:
        match damage_type:
            case DamageType.PHYSICAL:
                return damage - self.__calculate_defense(self.defense, self.defense_modifier)
            case DamageType.MAGIC:
                return damage - self.__calculate_defense(self.magic_defense, self.magic_defense_modifier)
            case _:
                return 1

    def __calculate_defense(self, attribute: int, modifier: float) -> int:
        return Number.round(attribute * modifier)

    def __check_negative_damage(self, damage: int) -> int:
        if damage <= 0:
            return 1
        else:
            return damage

    def __lose_hit_points(self, true_damage: int):
        self.hp -= true_damage

    def __check_alive_status(self):
        if self.hp <= 0:
            self.alive = False

    def caster_magic_power(self) -> int:
        return self.magic_power

    def caster_attack_power(self) -> int:
        return self.attack_power

    def has_weapon(self) -> bool:
        return self.weapon is not None

    def has_spells(self) -> bool:
        return len(self.spells) != 0
