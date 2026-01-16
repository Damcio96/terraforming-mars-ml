from dataclasses import dataclass

@dataclass(frozen=True)
class MapDefinition:
    base_types: tuple[TileBaseType, ...]
    bonuses: tuple[tuple[Bonus, ...], ...]
    neighbors: tuple[tuple[int, ...], ...]

    