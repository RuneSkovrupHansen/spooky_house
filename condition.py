class Condition:

    def __init__(self) -> None:
        pass

    # room_to_be_placed, game_context (floor, adjacent_rooms, existing rooms)

    # current_floor and adjacent_rooms = context
    def is_condition_ok(self, room_to_place, floor_type, adjacent_rooms, existing_rooms) -> bool:
        return True