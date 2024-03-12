class Weapon:
    __name: str
    __attack_power: int

    def __init__(self, name: str, attack_power: int):
        self.__name = name
        self.__attack_power = attack_power

    @property
    def name(self):
        return self.__name

    @property
    def attack_power(self):
        return self.__attack_power


