from game.state import GameState
from rules.masker import Masker
from rules.action_applier import ActionApplier
from player.human_player import HumanPlayer

class Game:
    def __init__(
        self,
        state: GameState,
        players: list[HumanPlayer],
        masker: Masker,
        applier: ActionApplier,
    ):
        self.state = state
        self.players = players
        self.masker = masker
        self.applier = applier

    def step(self):
        turn_info = self.state.turn_info
        player = self.players[turn_info.current_player]
        mask = self.masker.compute_legal_mask(self.state)
        action = player.choose_action(self.state, mask)
        self.state = self.applier.apply(self.state, action)

    def run(self):
        while not self.is_game_over():
            self.step()

    def is_game_over(self) -> bool:
        return False

