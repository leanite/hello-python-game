from etc.Number import Number
from spells import SpellCaster
from spells.Spell import Spell


class Nightmare(Spell):
    def __init__(self):
        super().__init__()
        self._name = "Nightmare"
        self._mana_cost = 8
        self._base_damage = 13
        self._spell_modifier = 1.8

    def calculate_spell_damage(self, caster: SpellCaster) -> int:
        return Number.round(
            caster.caster_magic_power() * self._spell_modifier + self._base_damage
        )
