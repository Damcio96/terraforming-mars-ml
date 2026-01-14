from dataclasses import dataclass, replace

@dataclass(frozen=True)
class TurnInfo:
    generation: int
    first_player: int
    current_player: int
    passed_players: tuple[bool, ...]
    has_acted: bool

    def update(
        self,
        *,
        generation: int | None = None,
        first_player: int | None = None,
        current_player: int | None = None,
        passed_players: tuple[bool, ...] | None = None,
        has_acted: bool | None = None
    ) -> "TurnInfo":
        return replace(
            self,
            generation=self.generation if generation is None else generation,
            first_player=self.first_player if first_player is None else first_player,
            current_player=self.current_player if current_player is None else current_player,
            passed_players=self.passed_players if passed_players is None else passed_players,
            has_acted=self.has_acted if has_acted is None else has_acted
        )
