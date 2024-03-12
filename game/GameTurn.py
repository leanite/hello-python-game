from typing import List

from characters.Npc import Npc
from game.GameAction import GameAction
from game.GamePrinter import GamePrinter


class GameTurn:

    game_action: GameAction

    def __init__(self, heroes: List[Npc], monsters: List[Npc]):
        self.game_action = GameAction(heroes, monsters)

    def heroes_turn(self):
        GamePrinter.turn_text("Heroes")
        self.game_action.heroes_action()

    def monsters_turn(self):
        GamePrinter.turn_text("Monsters")
        self.game_action.monsters_action()