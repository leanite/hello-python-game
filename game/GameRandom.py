from typing import List

from characters.Npc import Npc
from etc.Number import Number
from spells.Spell import Spell


class GameRandom:

    @staticmethod
    def random_target_from_list(targets: List[Npc]) -> Npc:
        target_index = Number.random_with_lower_zero(len(targets))

        return targets[target_index]

    @staticmethod
    def is_attacker_using_spell(attacker: Npc) -> bool:
        return attacker.has_spells() and GameRandom.is_random_action_spell_action()

    @staticmethod
    def is_random_action_spell_action() -> bool:
        return Number.random_with_lower_one(10) <= 3

    @staticmethod
    def random_spell_by(attacker: Npc) -> Spell:
        spells: List[Spell] = attacker.spells
        spell_index: int = Number.random_with_lower_zero(len(spells))

        return spells[spell_index]


