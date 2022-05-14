from condition import Condition

class ConditionValidFloor(Condition):

    def __init__(self, valid_floors) -> None:
        super().__init__()
        self.valid_floors = valid_floors

    def is_condition_ok(self, context) -> bool:
        return context.floor_type in self.valid_floors

class ConditionMaxAppearances(Condition):

    def __init__(self, max_appearances) -> None:
        super().__init__()
        self.max_appearances = max_appearances

    def is_condition_ok(self, context) -> bool:
        no_appearances = 0
        for room in context.existing_rooms:
            if room.name == context.room_to_place.name:
                no_appearances+=1

        return no_appearances < self.max_appearances
        
class ConditionOnMapEdge(Condition):

    def is_condition_ok(self, context) -> bool:
        
        target_position = context.target_position

        return target_position[0] == 0 or target_position == context.map_.get_width