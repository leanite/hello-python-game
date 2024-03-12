from etc.Number import Number
from spells import SpellCaster
from spells.Spell import Spell


class Fireball(Spell):
    def __init__(self):
        super().__init__()
        self._name = "Fireball"
        self._mana_cost = 6
        self._base_damage = 10
        self._spell_modifier = 1.8

    def calculate_spell_damage(self, caster: SpellCaster) -> int:
        return Number.round(
            caster.caster_magic_power() * self._spell_modifier + Number.random_with_lower_one(self._base_damage)
        )
