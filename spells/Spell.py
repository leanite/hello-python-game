from abc import ABC, abstractmethod
from typing import List

from spells import SpellCaster


class Spell(ABC):

    _name: str
    _mana_cost: int
    _base_damage: int
    _spell_modifier: float

    @abstractmethod
    def calculate_spell_damage(self, caster: SpellCaster) -> int:
        pass

    @property
    def name(self):
        return self._name

    @property
    def mana_cost(self):
        return self._mana_cost

    @property
    def base_damage(self):
        return self._base_damage

    @property
    def spell_modifier(self):
        return self._spell_modifier