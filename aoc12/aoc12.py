class Grid():

    def __init__(self, lines):
        self.grid = lines
        self.get_start_and_summit()
        self.positions = {}

    def get_start_and_summit(self):
        for idx, l in enumerate(self.grid):
            if "S" in l:
                self.start_pos = (idx, l.index("S"))
            if "E" in l:
                self.summit_pos = (idx, l.index("E"))

class Position():
    def __init__(self, coords, grid):
        self.coords = coords
        self.grid = grid
        self.char = grid.grid[coords[0]][coords[1]]
        self.grid.positions[coords] = self
        self.distance_to_summit = 10000000  # arbitrary big number
        if coords == grid.summit_pos:
            self.height = ord("z")
            self.distance_to_summit = 0
        elif coords == grid.start_pos:
            self.height = ord("a")
        else:
            self.height = ord(self.char)
        self.neighbors = []

    def get_neighbors(self):
        new_neighbors = []
        for y, x in [(self.coords[0] - 1, self.coords[1]),
                     (self.coords[0] + 1, self.coords[1]),
                     (self.coords[0], self.coords[1] - 1),
                     (self.coords[0], self.coords[1] + 1)]:
            if not 0 <= y < len(self.grid.grid):
                continue
            if not 0 <= x < len(self.grid.grid[0]):
                continue

            if (y, x) in self.grid.positions:
                if self.grid.positions[(y, x)] not in self.neighbors:
                    self.neighbors.append(self.grid.positions[(y, x)])
                continue

            neighbor = Position((y, x), self.grid)
            self.neighbors.append(neighbor)
            new_neighbors.append(neighbor)

        for nn in new_neighbors:
            nn.neighbors.append(self)
            nn.get_neighbors()

    def can_reach(self, neighbor):
        if self.height > neighbor.height or self.height in [neighbor.height, neighbor.height - 1]:
            return True
        return False

    def fill_distances(self):
        for neighbor in self.neighbors:
            if neighbor.can_reach(self):
                if (self.distance_to_summit + 1) < neighbor.distance_to_summit:
                    neighbor.distance_to_summit = self.distance_to_summit + 1
                    neighbor.fill_distances()


def main():
    lines = [i.strip() for i in open("input.txt")]
    grid = Grid(lines)
    summit = Position(grid.summit_pos, grid)
    summit.get_neighbors()
    summit.fill_distances()

    print("Distance from start to summit (part 1) -", grid.positions[grid.start_pos].distance_to_summit)
    min_a_dist = min([grid.positions[k].distance_to_summit for k in grid.positions if grid.positions[k].char == "a"])
    print("Least possible distance from an 'a' start site (part 2) -", min_a_dist)


if __name__ == "__main__":
    main()