from etc.Number import Number
from spells import SpellCaster
from spells.Spell import Spell


class EnergyWave(Spell):
    def __init__(self):
        super().__init__()
        self._name = "Energy Wave"
        self._mana_cost = 10
        self._base_damage = 15
        self._spell_modifier = 2.0

    def calculate_spell_damage(self, caster: SpellCaster) -> int:
        return Number.round(
            caster.caster_magic_power() * self._spell_modifier + self._base_damage
        )
