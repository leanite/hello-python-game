from etc.Number import Number
from spells import SpellCaster
from spells.Spell import Spell


class DoubleAttack(Spell):
    def __init__(self):
        super().__init__()
        self._name = "Double Attack"
        self._mana_cost = 12
        self._base_damage = 0
        self._spell_modifier = 2.5

    def calculate_spell_damage(self, caster: SpellCaster) -> int:
        return Number.round(
            caster.caster_attack_power() * self._spell_modifier
        )
