from dataclasses import dataclass

@dataclass(frozen=True)
class Tile:
    id: int
    base_type: TileBaseType
    special: HexSpecial
    occupant: TileOccupant
    bonuses: tuple[Bonus, ...]