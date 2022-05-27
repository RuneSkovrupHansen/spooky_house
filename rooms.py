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
        Lounge,
        UtilityRoom,
        HobbyRoom,
        LivingRoom,
        HomeTheater,
        AlterRoom,
        DollRoom,
        AlterRoom,
        WitchesDen,
        RottenRoom,
        GuestRoom,
        ControlRoom
        ]
    return room_list


class Hallway(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Hallway", 
            description="", 
            conditions=[], 
            lighting=1, 
            evilness=1)

class Kitchen(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Kitchen", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1)

class Pantry(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Pantry", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1)

class Bedroom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Bedroom", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1)

class WineCellar(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Wine Cellar", 
            description="", 
            conditions=[ConditionValidFloor(valid_floors=[FloorType.BASEMENT])],
            lighting=1, 
            evilness=1)

class GameRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Game Room", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1)

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
            evilness=1)

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
            prob_item=0.2)

class DiningRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Dining Room", 
            description="", 
            conditions=[
                ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER])
                ],
            lighting=1, 
            evilness=1)

class PrayerRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Prayer Room", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1,
            prob_event=0.33)

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
            prob_item=0.33,
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
            prob_event=0.75)

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
            prob_item=0.15)

class Bathroom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Bathroom", 
            description="", 
            conditions=[],
            lighting=1, 
            evilness=1)

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
            prob_event=0.4)

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
            prob_item=0.2)

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
            prob_event=0.4)

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
            prob_item=0.0,
            prob_event=0.0)

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
            prob_item=0.0,
            prob_event=0.0)

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
            evilness=1)

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
            evilness=1)

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
            prob_item=0.2,
            prob_event=0.4)

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
            prob_item=1.0)

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
            prob_event=0.75)

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
            prob_item=0.25,
            prob_event=0.75)

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
            evilness=1)

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
            prob_item=0.33)

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
            prob_event=0.33)

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
            prob_event=0.75)

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
            prob_item=0.2,
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
            evilness=1)

class UtilityRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Utility Room",
            description="",
            conditions=[ConditionValidFloor(valid_floors=[FloorType.BASEMENT, FloorType.GROUND]),
                        ConditionMaxAppearances(max_appearances=2)],
            lighting=1,
            evilness=1,
            prob_item=0.33)

class HobbyRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Hobby Room",
            description="",
            conditions=[ConditionValidFloor(valid_floors=[FloorType.BASEMENT, FloorType.GROUND]),
                        ConditionMaxAppearances(max_appearances=2)],
            lighting=1,
            evilness=1,
            prob_item=0.2)

class LivingRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Living Room",
            description="",
            conditions=[ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER]),
                        ConditionMaxAppearances(max_appearances=2)],
            lighting=1,
            evilness=1)

class HomeTheater(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Home Theater",
            description="",
            conditions=[ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER]),
                        ConditionMaxAppearances(max_appearances=1)],
            lighting=1,
            evilness=1)

class AlterRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Alter Room",
            description="",
            conditions=[ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.BASEMENT]),
                        ConditionMaxAppearances(max_appearances=1)],
            lighting=1,
            evilness=1,
            prob_event=0.5)

class DollRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Doll Room",
            description="",
            conditions=[ConditionMaxAppearances(max_appearances=1)],
            lighting=1,
            evilness=1,
            prob_event=0.75)

class WitchesDen(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Witch's Den",
            description="",
            conditions=[ConditionValidFloor(valid_floors=[FloorType.BASEMENT, FloorType.UPPER]),
                        ConditionMaxAppearances(max_appearances=1)],
            lighting=1,
            evilness=1,
            prob_item=0.33,
            prob_event=0.75)

class RottenRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Rotten Room",
            description="",
            conditions=[ConditionValidFloor(valid_floors=[FloorType.BASEMENT]),
                        ConditionMaxAppearances(max_appearances=1)],
            lighting=1,
            evilness=1,
            prob_event=0.5)

class GuestRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="Guest Room",
            description="",
            conditions=[ConditionValidFloor(valid_floors=[FloorType.GROUND, FloorType.UPPER]),
                        ConditionMaxAppearances(max_appearances=1)],
            lighting=1,
            evilness=1)

class ControlRoom(Room):
    def __init__(self) -> None:
        super().__init__(
            name="The Control Room",
            description="",
            conditions=[ConditionMaxAppearances(max_appearances=1)],
            lighting=1,
            evilness=1,
            prob_item=0.25)

# Ideas :
# Garage, Walk-in closet, fitness room, in-door swimming pool, sauna, walk-in freezer witch's den