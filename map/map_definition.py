from dataclasses import dataclass
from map.map_template import MapTemplate
from state.board import Board
from state.tile import Tile
from map.tile_definition import TileOccupant

@dataclass(frozen=True)
class MapDefinition:
    base_map: MapTemplate
    neighbors: tuple[tuple[int, ...], ...]

    def build_initial_board(self) -> Board:
        tiles = tuple(Tile(
                id=i,
                base_type=self.base_map.base_types[i],
                bonuses=self.base_map.bonuses[i],
                occupant=TileOccupant.EMPTY,
            )
            for i in range(len(self.base_map.base_types))
        )

        return Board(
            tiles=tiles,
            neighbors=self.neighbors,
            temperature = -30,
            oxygen = 0,
            oceans = 0,
        )

    