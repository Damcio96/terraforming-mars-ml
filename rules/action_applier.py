from actions.action_type import ActionType
from game.state import GameState
from game.turn_info import TurnInfo
import logging

logger = logging.getLogger(__name__)

class ActionApplier:

    def _advance_turn(self, turn_info: TurnInfo) -> TurnInfo:
        passed = list(turn_info.passed_players)
        n = len(passed)
        next_player = turn_info.current_player

        while True:
            next_player = (next_player + 1) % n
            if not passed[next_player]:
                return turn_info.update(current_player=next_player)
            
    def apply(self, state: GameState, action: ActionType) -> GameState:
        if action == ActionType.PASS:
            return self._apply_pass(state)

        raise NotImplementedError(action)

    def _apply_pass(self, state: GameState) -> GameState:
        passed = list(state.turn_info.passed_players)
        passed[state.turn_info.current_player] = True
        temp_turn_info = state.turn_info.update(passed_players=tuple(passed))

        if all(passed):
            logger.debug("\nThe action phase ends. \nThe generation %s has ended.", state.turn_info.generation)
            n = len(passed)
            new_first = (state.turn_info.first_player + 1) % n
            new_turn_info = temp_turn_info.update(
                generation=state.turn_info.generation + 1,
                first_player = new_first,
                current_player = new_first,
                passed_players = tuple(False for _ in passed)
            )
        else:
            new_turn_info = self._advance_turn(temp_turn_info)
        
        return GameState(
            players=state.players,
            board=state.board,
            turn_info=new_turn_info
        )
