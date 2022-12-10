class Rope():
    DIR_MOVES = {
        "R": [0, 1],
        "L": [0, -1],
        "U": [1, 1],
        "D": [1, -1]
    }

    def __init__(self, length):
        self.length = length
        self.head_pos, self.tail_pos = [0, 0], [0, 0]
        self.tail_positions_visited = [(0,0)]

    def move_head(self, direction):
        self.head_pos[Rope.DIR_MOVES[direction][0]] += Rope.DIR_MOVES[direction][1]

        x_delta = self.head_pos[0] - self.tail_pos[0]
        y_delta = self.head_pos[1] - self.tail_pos[1]

        if max([abs(x_delta), abs(y_delta)]) > self.length:
            self.pull_tail(x_delta, y_delta)

        if not tuple(self.tail_pos) in self.tail_positions_visited:
            self.tail_positions_visited.append(tuple(self.tail_pos))

    def pull_tail(self, x_delta, y_delta):
        if x_delta < 0:
            self.tail_pos[0] -= 1
        elif x_delta >0:
            self.tail_pos[0] += 1

        if y_delta < 0:
            self.tail_pos[1] -= 1
        elif y_delta > 0:
            self.tail_pos[1] += 1


def main():
    rope = Rope(10)
    for line in open("input.txt"):
        direction, distance = line.strip().split(" ")

        for i in range(int(distance)):
            rope.move_head(direction)

    print("Num positions visited by tail - ", len(rope.tail_positions_visited))

if __name__ == "__main__":
    main()