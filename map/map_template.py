from dataclasses import dataclass
from map.tile_definition import TileBaseType, Bonus

@dataclass(frozen=True)
class MapTemplate:
    base_types: tuple[TileBaseType,...]
    bonuses: tuple[tuple[Bonus, ...],...]