from typing import List

from characters.Npc import Npc
from characters.NpcBuilder import NpcBuilder
from items.Weapon import Weapon
from spells.DoubleAttack import DoubleAttack
from spells.EnergyWave import EnergyWave
from spells.Fireball import Fireball
from spells.Nightmare import Nightmare


def build_heroes() -> List[Npc]:
    return [__build_warrior(), __build_mage()]


def build_monsters() -> List[Npc]:
    return [__build_skeleton(), __build_slime(), __build_black_mage()]


def __build_warrior():
    return (
        NpcBuilder().create_warrior()
        .name("Glenn")
        .hp(120)
        .mana(40)
        .attack_power(18)
        .magic_power(3)
        .defense(13)
        .magic_defense(6)
        .weapon(Weapon(name="Great Sword", attack_power=15))
        .spells([DoubleAttack()])
        .build()
    )


def __build_mage():
    return (
        NpcBuilder().create_mage()
        .name("Azalea")
        .hp(90)
        .mana(110)
        .attack_power(5)
        .magic_power(22)
        .defense(6)
        .magic_defense(19)
        .weapon(Weapon(name="Rod", attack_power=7))
        .spells([Fireball(), EnergyWave()])
        .build()
    )


def __build_skeleton():
    return (
        NpcBuilder().create_skeleton()
        .name("Skeleton")
        .hp(80)
        .mana(0)
        .attack_power(12)
        .magic_power(0)
        .defense(9)
        .magic_defense(8)
        .weapon(Weapon(name="Bone Sword", attack_power=12))
        .build()
    )


def __build_slime():
    return (
        NpcBuilder().create_slime()
        .name("Slime")
        .hp(60)
        .mana(0)
        .attack_power(10)
        .magic_power(0)
        .defense(8)
        .magic_defense(5)
        .build()
    )


def __build_black_mage():
    return (
        NpcBuilder().create_black_mage()
        .name("Black Mage")
        .hp(150)
        .mana(120)
        .attack_power(5)
        .magic_power(20)
        .defense(8)
        .magic_defense(15)
        .weapon(Weapon(name="Dark Rod", attack_power=8))
        .spells([Nightmare()])
        .build()
    )
