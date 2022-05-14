import random

from card import Card
from room import Room
from rooms import get_all_rooms
from floor_type import FloorType

class CardGenerator:

    def __init__(self) -> None:
        self.all_rooms = get_all_rooms()

    def generate_card(self, context) -> Card:
        while True:
            all_conditions_ok = True
            index = random.randint(0, len(self.all_rooms)-1)
            generated_card = self.all_rooms[index]()
            context.room_to_place = generated_card
            if isinstance(generated_card, Room):
                for condition in generated_card.conditions:
                    if not condition.is_condition_ok(context):
                        all_conditions_ok = False
                        break
                
                if all_conditions_ok:
                    break
        
        return generated_card
