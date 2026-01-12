from abc import ABC, abstractmethod
from game.state import GameState
from actions.action_type import ActionType
import numpy as np

class Player(ABC):

    @abstractmethod
    def choose_action(
        self,
        state,
        mask: np.ndarray
    ) -> ActionType:
        ...



