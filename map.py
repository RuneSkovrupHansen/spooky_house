class Map:

    def __init__(self, rows, cols) -> None:

        self.rows = rows
        self.cols = cols

        self.map = []
        for _ in range(rows):
            col = []
            for _ in range(cols):
                col.append(None)
            
            self.map.append(col)
        
    def __repr__(self) -> str:
        return self._get_map_string()
    
    def insert_element(self, element, row, col):
        self.map[row][col] = element

    def remove_element(self, row, col):
        self.map[row][col] = None

    def get_element(self, row, col):
        return self.map[row][col]

    def get_height(self):
        return self.rows

    def get_width(self):
        return self.cols

def print_map(map_, player_position):
    map_string = ""

    for i, row in enumerate(map_.map):
        for j, element in enumerate(row):
            if player_position == (i,j):
                map_string += " o "
            elif element is None:
                map_string += f" . "
            else:
                map_string += " x "

        map_string += "\n"
    
    print(map_string)