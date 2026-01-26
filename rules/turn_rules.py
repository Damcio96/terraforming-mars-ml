from state.turn_info import TurnInfo

class TurnRules:

    # @staticmethod
    # def advance_turn(turn_info: TurnInfo) -> TurnInfo:
    #     if not turn_info.has_acted:
    #         return turn_info.update(has_acted=True)

    #     passed_players = list(turn_info.passed_players)
    #     next_player = turn_info.current_player

    #     while True:
    #         next_player = (next_player + 1) % len(passed_players)
    #         if not passed_players[next_player]:
    #             return turn_info.update(current_player=next_player, has_acted=False)
            
    @staticmethod
    def advance_turn(turn_info: TurnInfo) -> TurnInfo:
        if not turn_info.has_acted:
            return turn_info.update(has_acted=True)      
        return TurnRules.advance_player(turn_info)   

    @staticmethod
    def advance_player(turn_info: TurnInfo) -> TurnInfo:
        passed_players = list(turn_info.passed_players)
        next_player = turn_info.current_player

        while True:
            next_player = (next_player + 1) % len(passed_players)
            if not passed_players[next_player]:
                return turn_info.update(current_player=next_player, has_acted=False)