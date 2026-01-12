from dataclasses import dataclass, replace

@dataclass(frozen=True)
class PlayerState:
    id: int
    #corporation: int
    terraforming_rating: int

    credits: int
    #steel: int
    #titanium: int
    #plants: int
    #energy: int
    #heat: int

    production_credits: int
    #production_steel: int
    #production_titanium: int
    #production_plants: int
    #production_energy: int
    #production_heat: int

    tiles_total: int
    city_tiles: int
    greenery_tiles: int

    #events: int
    #buildings: int
    #space: int
    #power: int
    #science: int
    #jovian: int
    #earth: int
    #plant: int
    #microbe: int
    #animals: int
    #city: int

    def update(
        self,
        *,
        terraforming_rating: int | None = None,
        credits: int | None = None,
        production_credits: int | None = None,
        tiles_total: int | None = None,
        city_tiles: int | None = None,
        greenery_tiles: int | None = None,
        ) -> "PlayerState":
            return replace(
            self,
            terraforming_rating=self.terraforming_rating if terraforming_rating is None else terraforming_rating,
            credits=self.credits if credits is None else credits,
            production_credits=self.production_credits if production_credits is None else production_credits,
            tiles_total=self.tiles_total if tiles_total is None else tiles_total,
            city_tiles=self.city_tiles if city_tiles is None else city_tiles,
            greenery_tiles=self.greenery_tiles if greenery_tiles is None else greenery_tiles,
            )

