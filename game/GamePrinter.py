from characters.Npc import Npc
from spells.Spell import Spell


class GamePrinter:

    @staticmethod
    def turn_text(group_name: str):
        print(f"c====[] {group_name}' turn   =====>")

    @staticmethod
    def vertical_space():
        print()

    @staticmethod
    def end_of_battle_text(winner_group: str):
        print(f"** {winner_group} won the battle! **")

    @staticmethod
    def spell_used_text(spell: Spell, attacker: Npc, target: Npc):
        print(f"{attacker.name} [{attacker.character_class}] used {spell.name} on {target.name} [{target.character_class}]!")

    @staticmethod
    def out_of_mana_text(spell: Spell, attacker: Npc):
        print(f"{attacker.name} [{attacker.character_class}] tried to use {spell.name}, but {attacker.name} was out of mana!")

    @staticmethod
    def attack_text(attacker: Npc, target: Npc):
        print(f"{attacker.name} [{attacker.character_class}] attacked {target.name} [{target.character_class}]!")

    @staticmethod
    def damage_text(target: Npc, damage: int):
        print(f"{target.name} took {damage} point(s) of damage!")

    @staticmethod
    def defeated_text(defeated: Npc):
        print(f"{defeated.name} [{defeated.character_class}] was defeated!")