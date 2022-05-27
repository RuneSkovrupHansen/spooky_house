from card_generator import CardGenerator
from floor_type import FloorType
from map import Map
from map import print_map
from condition_context import ConditionContext

import random

class GameHandler:

    movement_keys = {
        "w": (-1, 0),
        "a": (0, -1),
        "s": (1, 0),
        "d": (0, 1)
    }

    def __init__(self, card_generator, map, start_position) -> None:

        self.card_generator = card_generator
        self.map = map

        self.possible_inputs = list(self.movement_keys.keys())
        self.existing_cards = []
        self.current_position = start_position
        self.game_context = ConditionContext()
    
    def _get_user_input(self) -> str:
        inp = ""
        while inp not in self.possible_inputs:
            inp = input("Where do you want to go?\n")
            inp = inp.lower()
        
        return inp
    
    def _update_position(self, move):
        new_pos = (
            self.current_position[0] + self.movement_keys.get(move)[0],
            self.current_position[1] + self.movement_keys.get(move)[1]
        )

        self.current_position = new_pos
        print(self.current_position)  # y must not be < 0 or > map.width

    def _check_position_in_bounds(self, user_input):
        validity = True
        if self.current_position[1] == 0 and user_input == "a":
            validity = False
        elif self.current_position[1] == self.map.get_width() - 1 and user_input == "d":
            validity = False
        elif self.current_position[0] == 0 and user_input == "w":
            validity = False
        elif self.current_position[0] == self.map.get_height() - 1 and user_input == "s":
            validity = False

        return validity
    
    def _advance(self) -> None:

        while True:
            user_input = self._get_user_input()
            if self._check_position_in_bounds(user_input=user_input):  # check input is in bounds of map
                break

        self._update_position(user_input)

        card = self.map.get_element(*self.current_position)
        if card is None:
            self.game_context.target_position = self.current_position
            self.game_context.map_ = self.map
            self.game_context.floor_type = FloorType.BASEMENT
            self.game_context.existing_rooms = self.existing_cards
            card = self.card_generator.generate_card(self.game_context)
            self.existing_cards.append(card)
            self.map.insert_element(card, *self.current_position)

        print_map(self.map, self.current_position)
        print(card)

    def _game_loop(self):

        card = self.map.get_element(*self.current_position)
        self.game_context.target_position = self.current_position
        self.game_context.map_ = self.map
        self.game_context.floor_type = FloorType.BASEMENT
        self.game_context.existing_rooms = self.existing_cards
        card = self.card_generator.generate_card(self.game_context)
        self.existing_cards.append(card)
        self.map.insert_element(card, *self.current_position)
        

        print_map(self.map, self.current_position)
        print(card)

        while True:
            self._advance()
        
        # print("Game over!")
    
    def start_game(self):
        self._game_loop()


def main():

    card_generator = CardGenerator()

    # Initialize map with random size
    map_height = random.randint(4, 7)
    map_width = random.randint(4, 7)
    map_ = Map(map_height, map_width)

    # Random start position from map size
    start_position = (
        random.randint(0, map_height-1),
        random.randint(0, map_width-1)
    )

    game = GameHandler(card_generator, map_, start_position)

    game.start_game()

if __name__ == "__main__":
    main()