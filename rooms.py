from room import Room
from floor_type import FloorType
from conditions import *


def get_all_rooms() -> list:
    room_list = [
            Hallway,
            Kitchen,
            Pantry,
            Bedroom,
            WineCellar,
            GameRoom,
            Foyer,
            PortalRoom,
            Office,
            DiningRoom,
            PrayerRoom,
            GreenRoom,
            RedRoom,
            Library,
            Bathroom,
            CellRoom,
            ServantsQuarters,
            MirrorRoom,
            ColdRoom,
            TeaRoom,
            GalleryRoom,
            Laboratory,
            Armory,
            BoilerRoom,
            Nursery,
            MusicRoom,
            AstralObservatory,
            Larder,
            StorageRoom,
            BellTower,
            Tower,
            Furnace,
            TaxidermyRoom,
            Lounge
        ]
    return room_list


class Hallway(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Hallway", 
            description="", 
            conditions=[], 
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Kitchen(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Kitchen", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1,
            prob_item=0.1, 
            prob_event=0.5)

class Pantry(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Pantry", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Bedroom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Bedroom", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class WineCellar(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Wine Cellar", 
            description="", 
            conditions=[ConditionValidFloor(valid_floors=[FloorType.BASEMENT])],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class GameRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Game Room", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Foyer(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Foyer", 
            description="", 
            conditions=[
                ConditionValidFloor(valid_floors=[FloorType.GROUND]),
                ConditionMaxAppearances(max_appearances=1),
                ConditionOnMapEdge()
                ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class PortalRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Portal Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1)
                ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Office(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Office", 
            description="", 
            conditions=[
                ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class DiningRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Dining Room", 
            description="", 
            conditions=[
                ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER])
                ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class PrayerRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Prayer Room", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class GreenRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Green Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1)
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class RedRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Red Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1)
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Library(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Library", 
            description="", 
            conditions=[
                ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Bathroom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Bathroom", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class CellRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Cell Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=2),
                ConditionValidFloor(valid_floors=[FloorType.BASEMENT])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class ServantsQuarters(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Servants Quarters", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=2),
                ConditionValidFloor(valid_floors=[FloorType.BASEMENT])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class ColdRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Cold Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1),
                ConditionValidFloor(valid_floors=[FloorType.BASEMENT])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class MirrorRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Mirror Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1)
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class StairsAscending(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Ascending Stairs", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=2),
                ConditionValidFloor(valid_floors=[FloorType.BASEMENT, FloorType.GROUND])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class StairsDescending(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Descending Stairs", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=2),
                ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class TeaRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Tea Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=2),
                ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class GalleryRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Gallery Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=2),
                ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Laboratory(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Laboratory", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1),
                ConditionValidFloor(valid_floors=[FloorType.BASEMENT, FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Armory(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Armory", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1),
                ConditionValidFloor(valid_floors=[FloorType.GROUND])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class BoilerRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Boiler Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1),
                ConditionValidFloor(valid_floors=[FloorType.BASEMENT])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Nursery(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Nursery", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=2),
                ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class MusicRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Music Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1),
                ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class AstralObservatory(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Astral Observatory", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1),
                ConditionValidFloor(valid_floors=[FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Larder(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Larder", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=2),
                ConditionValidFloor(valid_floors=[FloorType.BASEMENT])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class StorageRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Storage Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1),
                ConditionValidFloor(valid_floors=[FloorType.BASEMENT, FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class BellTower(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Bell Tower", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1),
                ConditionValidFloor(valid_floors=[FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Tower(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Tower", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=2),
                ConditionValidFloor(valid_floors=[FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Furnace(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Furnace", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1),
                ConditionValidFloor(valid_floors=[FloorType.BASEMENT])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Botanica(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Botanica", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1),
                ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER]),
                ConditionOnMapEdge()
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class TaxidermyRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Taxidermy Room", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=1),
                ConditionValidFloor(valid_floors=[FloorType.GROUND])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)

class Lounge(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Lounge", 
            description="", 
            conditions=[
                ConditionMaxAppearances(max_appearances=2),
                ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER])
            ],
            lighting=1, 
            evilness=1, 
            prob_item=0.1, 
            prob_event=0.5)
