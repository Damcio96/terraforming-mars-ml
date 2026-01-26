from dataclasses import dataclass, replace
from state.player_state import PlayerState
from state.board import Board
from state.turn_info import TurnInfo

@dataclass(frozen=True)
class GameState:
    player_states: tuple[PlayerState, ...]
    board: Board
    turn_info: TurnInfo

    def update(
        self,
        *,
        player_states: tuple[PlayerState, ...] | None = None,
        board: Board | None = None,
        turn_info: TurnInfo | None = None,
    ) -> "GameState":
        return replace(
            self,
            player_states=self.player_states if player_states is None else player_states,
            board=self.board if board is None else board,
            turn_info=self.turn_info if turn_info is None else turn_info,
        )