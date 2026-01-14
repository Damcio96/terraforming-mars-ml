from player.player import Player
from game.state import GameState
from actions.action_type import ActionType

class HumanPlayer(Player):

    def choose_action(self, state: GameState, mask):
        legal_actions = [i for i, m in enumerate(mask) if m]

        player_index = state.turn_info.current_player
        player_id = state.player_states[player_index].id
        print("\nGeneration: ", state.turn_info.generation)
        print("Player: ", player_id)
        print(state.player_states[player_index])
        print("Legal actions:")
        for i in legal_actions:
            print(f"{i}: {ActionType(i).name}")

        while True:
            try:
                choice = int(input("Choose action: "))
                if choice in legal_actions:
                    return ActionType(choice)
            except ValueError:
                pass

            print("Invalid action, try again.")

