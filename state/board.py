from dataclasses import dataclass, replace
from state.tile import Tile

@dataclass(frozen=True)
class Board:

    tiles: tuple[Tile, ...]
    neighbors: tuple[tuple[int, ...], ...]

    max_temperature: int = 8
    max_oxygen: int = 14
    max_oceans: int = 9

    temperature: int = -30
    oxygen: int = 0
    oceans: int = 0

    terraformer: int | None = None
    mayor: int | None = None
    gardener: int | None = None
    builder: int | None = None
    planner: int | None = None

    landlord: int | None = None
    banker: int | None = None
    scientist: int | None = None
    thermalist: int | None = None
    miner: int | None = None

    def update(
            self,
            *,
            temperature: int | None = None,
            oxygen: int | None = None,
            oceans: int | None = None,
        ) -> "Board":
            return replace(
                self,
                temperature=self.temperature if temperature is None else temperature,
                oxygen=self.oxygen if oxygen is None else oxygen,
                oceans=self.oceans if oceans is None else oceans,
            )

    def update_milestones(
            self,
            *,
            terraformer: int | None = None,
            mayor: int | None = None,
            gardener: int | None = None,
            builder: int | None = None,
            planner: int | None = None,
        ) -> "Board":
            return replace(
                self,
                terraformer=self.terraformer if terraformer is None else terraformer,
                mayor=self.mayor if mayor is None else mayor,
                gardener=self.gardener if gardener is None else gardener,
                builder=self.builder if builder is None else builder,
                planner=self.planner if planner is None else planner,
            )

    def update_rewards(
            self,
            *,
        landlord: int | None = None,
        banker: int | None = None,
        scientist: int | None = None,
        thermalist: int | None = None,
        miner: int | None = None,
        ) -> "Board":
            return replace(
                self,
                landlord=self.landlord if landlord is None else landlord,
                banker=self.banker if banker is None else banker,
                scientist=self.scientist if scientist is None else scientist,
                thermalist=self.thermalist if thermalist is None else thermalist,
                miner=self.miner if miner is None else miner,
            )




