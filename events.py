from event_local import EventLocal


def get_all_local_events() -> list:
    events_list = [
        TicTocSound(),
        CreakingSound,
        WindCold
        ]
    return events_list


class TicTocSound(EventLocal):
    def __init__(self) -> None:
        super().__init__(
            name="Tic Toc Sound",
            description="As you step into the room, you notice a ticking sound coming from the far end of the room. "
                        "Tic toc. As you notice yourself looking for a watch, the ticking stops. "
                        "You stand in silence and listen for it, but it doesn't return. What could this mean?")


class CreakingSound(EventLocal):
    def __init__(self) -> None:
        super().__init__(
            name="Creaking Sound",
            description="Looking around, you find yourself alone in the room. A few moments passes by. "
                        "Suddenly you hear a slow, creaking sound, as if coming from a door being opened. "
                        "Have you begun hearing things that are not there?")


class WindCold(EventLocal):
    def __init__(self) -> None:
        super().__init__(
            name="Cold Wind",
            description="As you open the door, a cool wind hits you and gives you the chills. You stand in the door"
                        " for just a brief moment, and enter the room as your goosebumps begin to disappear.")
