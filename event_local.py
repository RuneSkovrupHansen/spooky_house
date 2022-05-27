class EventLocal:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description + f"This is a {self.name}"

    def get_info_string(self) -> str:
        return f"name: {self.name}\ndescription: {self.description}"

    def __repr__(self) -> str:
        return self.get_info_string()
