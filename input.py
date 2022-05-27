import time
import pygame

class InputHandler:

    def __init__(self, keys, timeout=None) -> None:
        self.keys = keys
        self.timeout = timeout

    def get_input(self):

        if self.timeout:
            timeout = time.time() + self.timeout

        pygame.event.clear()

        while True:

            if self.timeout and time.time() > timeout:
                return None

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key not in self.keys:
                        continue

                    return event.key

def main():

    pygame.init()

    # Display is required to get input 
    pygame.display.set_mode((100, 100))
    pygame.display.update()


    keys = [
        pygame.K_w,
        pygame.K_a,
        pygame.K_s,
        pygame.K_d
    ]

    movement_input_handler = InputHandler(keys)

    while True:
        print(chr(movement_input_handler.get_input()))

if __name__ == "__main__":
    main()
