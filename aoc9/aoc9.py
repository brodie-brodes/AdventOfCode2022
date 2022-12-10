class Rope():
    DIR_MOVES = {
        "R": [0, 1],
        "L": [0, -1],
        "U": [1, 1],
        "D": [1, -1]
    }

    def __init__(self, length, start_pos):
        self.length = length
        self.knots = {}
        self.lead_knot = Knot(rope=self, num_parents=0, start_pos=start_pos)
        self.tail = self.knots[max(self.knots.keys())]

    def pull(self, dir):
        self.lead_knot.move(dir)
        self.lead_knot.update_next_knot()

    def show_rope_in_grid(self, grid_dims=(30, 30)):
        grid = []
        for i in range(grid_dims[1]):
            r = []
            for j in range(grid_dims[0]):
                r.append(".")

            grid.append(r)

        knots_rev = list(self.knots.keys())
        knots_rev.reverse()

        for k in knots_rev:
            x, y = self.knots[k].pos
            y = -y - 1
            grid[y][x] = str(k)
        for l in grid:
            print("".join(l))


class Knot():

    def __init__(self, rope, num_parents, start_pos):
        self.rope = rope
        self.rope.knots[num_parents] = self
        self.num_parents = num_parents
        self.pos = start_pos

        if num_parents < rope.length - 1:
            self.next_knot = Knot(rope=rope, num_parents=num_parents + 1, start_pos=self.pos.copy())
        else:
            self.next_knot = None

        self.positions_visited = [tuple(self.pos)]

    def move(self, direction):
        self.pos[Rope.DIR_MOVES[direction][0]] += Rope.DIR_MOVES[direction][1]


    def update_next_knot(self):
        if self.next_knot == None:
            return ""
        x_delta = self.pos[0] - self.next_knot.pos[0]
        y_delta = self.pos[1] - self.next_knot.pos[1]

        if max([abs(x_delta), abs(y_delta)]) > 1:
            self.pull_next_knot(x_delta, y_delta)



        self.next_knot.update_next_knot()
        self.next_knot.update_positions_visited()

    def update_positions_visited(self):
        if tuple(self.pos) not in self.positions_visited:
            self.positions_visited.append(tuple(self.pos))


    def pull_next_knot(self, x_delta, y_delta):
        if x_delta < 0:
            self.next_knot.move("L")
        elif x_delta > 0:
            self.next_knot.move("R")

        if y_delta < 0:
            self.next_knot.move("D")
        elif y_delta > 0:
            self.next_knot.move("U")




def main():
    rope = Rope(10, start_pos=[12,5])

    for move in open("input.txt"):
        direction, distance = move.strip().split(" ")
        for m in range(int(distance)):
            rope.pull(direction)

    print("Number of positions visited by tail - ", len(rope.tail.positions_visited))



if __name__ == "__main__":
    main()