from dataclasses import dataclass, replace
from game.player_state import PlayerState
from game.board import Board
from game.turn_info import TurnInfo

@dataclass(frozen=True)
class GameState:
    players: tuple[PlayerState, ...]
    board: Board
    turn_info: TurnInfo

    def update(
        self,
        *,
        players: tuple[PlayerState, ...] | None = None,
        board: Board | None = None,
        turn_info: TurnInfo | None = None,
    ) -> "GameState":
        return replace(
            self,
            players=self.players if players is None else players,
            board=self.board if board is None else board,
            turn_info=self.turn_info if turn_info is None else turn_info,
        )