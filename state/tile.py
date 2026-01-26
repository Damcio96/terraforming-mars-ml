from dataclasses import dataclass
from map.tile_definition import TileBaseType, TileOccupant, Bonus

@dataclass(frozen=True)
class Tile:
    id: int
    base_type: TileBaseType
    occupant: TileOccupant
    bonuses: tuple[Bonus, ...]