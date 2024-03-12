from game.GameBuilder import build_heroes, build_monsters
from game.GamePrinter import GamePrinter
from game.GameTurn import GameTurn


class Game:
    __turn: GameTurn

    def __init__(self):
        self.__turn = GameTurn(build_heroes(), build_monsters())

    def loop(self):
        while True:
            self.battle_turn()

    def battle_turn(self):
        self.__turn.heroes_turn()
        self.__turn.monsters_turn()
        GamePrinter.vertical_space()