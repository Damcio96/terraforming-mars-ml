from state.state import GameState
from state.turn_info import TurnInfo

class GenerationRules:

    @staticmethod
    def end_generation(state: GameState) -> GameState:
        updated_player_states = GenerationRules.apply_production_phase(state)
        next_first_player = (state.turn_info.first_player + 1) % len(state.turn_info.passed_players)
        
        updated_turn_info = state.turn_info.update(
            generation=state.turn_info.generation + 1,
            first_player=next_first_player,
            current_player=next_first_player,
            passed_players=tuple(False for _ in state.turn_info.passed_players),
            has_acted=False
        )

        return state.update(player_states=updated_player_states, turn_info=updated_turn_info)

    @staticmethod
    def apply_production_phase(state: GameState) -> tuple:
        updated_player_states = []
        for ps in state.player_states:
            credits_income = ps.production_credits + ps.terraforming_rating
            updated_player_states.append(ps.update(credits = ps.credits + credits_income))
        return tuple(updated_player_states)