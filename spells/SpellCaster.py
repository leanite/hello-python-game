from abc import ABC, abstractmethod


class SpellCaster(ABC):

    @abstractmethod
    def caster_magic_power(self) -> int:
        pass

    @abstractmethod
    def caster_attack_power(self) -> int:
        pass
