from actions.action_type import ActionType
from game.state import GameState
from game.turn_info import TurnInfo
from rules.turn_rules import TurnRules
from rules.generation_rules import GenerationRules
import logging

logger = logging.getLogger(__name__)

class ActionApplier:
            
    def apply(self, state: GameState, action: ActionType) -> GameState:
        if action == ActionType.PASS:
            return self._apply_pass(state)
        if action == ActionType.WAIT:
            return self._apply_wait(state)
        if action == ActionType.ASTEROID:
            return self._apply_asteroid(state)

        logger.debug("ActionApplier received action: %s (%s)", action, int(action))
        raise NotImplementedError(action)

    def _apply_wait(self, state: GameState) -> GameState:
        updated_turn_info = TurnRules.advance_turn(state.turn_info)
        return state.update(turn_info=updated_turn_info)

    def _apply_pass(self, state: GameState) -> GameState:
        passed = list(state.turn_info.passed_players)
        passed[state.turn_info.current_player] = True
        updated_turn_info = state.turn_info.update(passed_players=tuple(passed))

        if all(passed):
            logger.debug("\nThe action phase ends. \nThe generation %s has ended.", updated_turn_info.generation)
            return GenerationRules.end_generation(state=state.update(turn_info=updated_turn_info))
        else:
            updated_turn_info = TurnRules.advance_player(updated_turn_info)
            return state.update(turn_info=updated_turn_info)
    
    def _apply_asteroid(self, state: GameState) -> GameState:
        cp = state.turn_info.current_player
        player_state = state.player_states[cp]
        updated_player_state = player_state.update(
            credits=player_state.credits - 14,
            terraforming_rating=player_state.terraforming_rating + 1
        )
        updated_player_states = list(state.player_states)
        updated_player_states[cp] = updated_player_state
        updated_board = state.board.update(temperature=state.board.temperature + 1)
        updated_turn_info = TurnRules.advance_turn(state.turn_info)

        return state.update(player_states=tuple(updated_player_states), board=updated_board, turn_info=updated_turn_info)


