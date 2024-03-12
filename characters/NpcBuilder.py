from typing import List

from characters.Npc import Npc
from items.Weapon import Weapon
from spells.Spell import Spell


class NpcBuilder:
    __npc: Npc

    def __init__(self):
        self.__npc = Npc()
        self.__npc.alive = True
        self.__npc.spells = []
        self.__npc.weapon = None

    def create_warrior(self) -> 'NpcBuilder':
        self.__npc.character_class = "Warrior"
        self.__npc.attack_modifier = 1.7
        self.__npc.defense_modifier = 1.5
        self.__npc.magic_defense_modifier = 0.85

        return self

    def create_mage(self) -> 'NpcBuilder':
        self.__npc.character_class = "Mage"
        self.__npc.attack_modifier = 1.0
        self.__npc.defense_modifier = 0.7
        self.__npc.magic_defense_modifier = 2.0

        return self

    def create_skeleton(self) -> 'NpcBuilder':
        self.__npc.character_class = "Monster"
        self.__npc.attack_modifier = 1.5
        self.__npc.defense_modifier = 1.1
        self.__npc.magic_defense_modifier = 1.1

        return self

    def create_slime(self) -> 'NpcBuilder':
        self.__npc.character_class = "Monster"
        self.__npc.attack_modifier = 1.0
        self.__npc.defense_modifier = 0.9
        self.__npc.magic_defense_modifier = 0.9

        return self

    def create_black_mage(self) -> 'NpcBuilder':
        self.__npc.character_class = "Monster"
        self.__npc.attack_modifier = 1.0
        self.__npc.defense_modifier = 0.95
        self.__npc.magic_defense_modifier = 1.85

        return self

    def name(self, name: str) -> 'NpcBuilder':
        self.__npc.name = name

        return self

    def hp(self, hp: int) -> 'NpcBuilder':
        self.__npc.hp = hp

        return self

    def mana(self, mana: int) -> 'NpcBuilder':
        self.__npc.mana = mana

        return self

    def attack_power(self, attack_power: int) -> 'NpcBuilder':
        self.__npc.attack_power = attack_power

        return self

    def magic_power(self, magic_power: int) -> 'NpcBuilder':
        self.__npc.magic_power = magic_power

        return self

    def defense(self, defense: int) -> 'NpcBuilder':
        self.__npc.defense = defense

        return self

    def magic_defense(self, magic_defense: int) -> 'NpcBuilder':
        self.__npc.magic_defense = magic_defense

        return self

    def weapon(self, weapon: Weapon) -> 'NpcBuilder':
        self.__npc.weapon = weapon

        return self

    def spells(self, spells: List[Spell]) -> 'NpcBuilder':
        self.__npc.spells = spells

        return self

    def build(self) -> Npc:
        return self.__npc
