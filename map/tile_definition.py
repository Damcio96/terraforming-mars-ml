from enum import Enum

class TileBaseType(Enum):
    NORMAL = 0
    OCEAN_ONLY = 1
    RESERVED = 2

class Bonus(Enum):
    CARD = 0
    STEEL = 1
    TITANIUM = 2
    PLANT = 3