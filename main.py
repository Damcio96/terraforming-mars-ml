from game.game import Game
from game.state import GameState
from game.board import Board
from game.turn_info import TurnInfo
from game.player_state import PlayerState
from rules.masker import Masker
from rules.action_applier import ActionApplier
from player.human_player import HumanPlayer
import logging

logging.basicConfig(
    level=logging.DEBUG,   #INFO / WARNING / ERROR
    format="%(message)s"
)

def main():
    player_states = tuple(
        PlayerState(
            id=i,
            terraforming_rating=20,
            credits=20,
            production_credits=0,
            tiles_total=0,
            city_tiles=0,
            greenery_tiles=0,
        )
        for i in range(2)
    )

    state = GameState(
        player_states=player_states,
        board=Board(),
        turn_info=TurnInfo(
            generation = 1,
            first_player = 0,
            current_player = 0,
            passed_players=(False, False),
            has_acted=False
        ),
    )

    players = [
        HumanPlayer(),
        HumanPlayer(),
    ]

    game = Game(
        state=state,
        players=players,
        masker=Masker(),
        applier=ActionApplier(),
    )

    game.run()

if __name__ == "__main__":
    main()
