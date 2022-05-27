import random

import card
from events import get_all_local_events

class Room(card.Card):

    def __init__(self, name, description, conditions, lighting, evilness, prob_item, prob_event) -> None:

        self.name = name
        self.description = description

        self.conditions = conditions

        # Consider passing to get_description
        self.lighting = lighting # 1-10
        self.evilness = evilness # 1-10

        self.prob_item = prob_item
        self.prob_event = prob_event

        self.event_local = None

        self.connections = []

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description + f"This is a {self.name}"

    def get_conditions(self):
        return self.conditions

    def get_lighting(self):
        return self.lighting

    def get_evilness(self):
        return self.evilness

    def get_prob_item(self):
        return self.prob_item

    def get_prob_event(self):
        return self.prob_event

    def get_info_string(self) -> str:
        return f"name: {self.name}\ndescription: {self.description}"

    def __repr__(self) -> str:
        return self.get_info_string()

    # Override
    def on_room_generated(self):
        print(self)
        trigger_event = random.random() > self.prob_event
        trigger_item = random.random() > self.prob_item

        if trigger_event:
            possible_events = get_all_local_events()
            self.event_local = possible_events[random.randint(0, len(possible_events))]()  # get a random event
            print(self.event_local)
