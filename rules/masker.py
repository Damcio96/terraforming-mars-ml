import numpy as np
from actions.action_type import ActionType
from game.state import GameState
#from actions.action_group import ActionGroup, ACTION_GROUP

class Masker:
    def compute_legal_mask(self, state: GameState) -> np.ndarray:
        mask = np.zeros(len(ActionType), dtype=np.int8)

        cp = state.turn_info.current_player

        if not state.turn_info.passed_players[cp]:
            mask[ActionType.PASS] = 1

        return mask

    # def _mask_turn_actions(self, mask):
    #     if self.action_number == 0:
    #         mask[ActionType.PASS] = True
    #     elif self.action_number == 1:
    #         mask[ActionType.WAIT] = True

    # def _mask_standard_projects(self, mask):
    #     if self.action_number != 0:
    #         return

    #     for action, group in ACTION_GROUP.items():
    #         if group is ActionGroup.STANDARD_PROJECT:
    #             if self._can_do_standard_project(action):
    #                 mask[action] = True

    # def _can_do_standard_project(self, action: ActionType) -> bool:
    #     cost = self.get_standard_project_cost(action)
    #     return self.resources.can_pay(cost)