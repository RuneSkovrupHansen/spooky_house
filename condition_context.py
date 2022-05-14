class ConditionContext:

    def __init__(self, room_to_place=None, target_position=None, map_=None, floor_type=None, existing_rooms=None) -> None:
        self.room_to_place = room_to_place
        self.target_position = target_position
        self.map_ = map_
        self.floor_type = floor_type
        self.existing_rooms = existing_rooms