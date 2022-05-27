import card

class Room(card.Card):

    def __init__(self, name, description, conditions, lighting, evilness, prob_item=0.1, prob_event=0.25) -> None:

        self.name = name
        self.description = description

        self.conditions = conditions

        # Consider passing to get_description
        self.lighting = lighting # 1-10
        self.evilness = evilness # 1-10

        self.prob_item = prob_item
        self.prob_event = prob_event

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
    def on_card_draw(self):
        self.print_info()
