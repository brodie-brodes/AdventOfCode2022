"""Ugliest code below :) """

def make_grid(p2 = False):
    max_x, max_y = 0, 0
    for line in open("input.txt"):
        coords = line.strip().split(" -> ")
        for coord in coords:
            x, y = [int(e) for e in coord.split(",")]
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

    grid = []
    for i in range(max_y + 1):
        grid.append(list("." * (max_x + 1)))

    if p2:
        grid.append(list("." * (max_x + 1)))
        grid.append(list("#" * (max_x + 1)))

    return grid

def add_path_to_grid(grid, path):
    coords = path.strip().split(" -> ")
    for idx in range(1, len(coords)):
        coord1 = coords[idx -1]
        coord2 = coords[idx]

        x1, y1 = [int(e) for e in coord1.split(",")]
        x2, y2 = [int(e) for e in coord2.split(",")]

        x_pos, y_pos = x1, y1
        x_delta = -1 if x1 > x2 else 1
        y_delta = -1 if y1 > y2 else 1

        grid[y_pos][x_pos] = "#"

        while x_pos != x2:
            x_pos += x_delta
            grid[y_pos][x_pos] = "#"

        while y_pos != y2:
            y_pos += y_delta
            grid[y_pos][x_pos] = "#"

def add_rock_to_grid(grid):
    for line in open("input.txt"):
        add_path_to_grid(grid, line.strip())

def add_sand(grid):
    y_pos, x_pos = 0, 500
    at_rest = False
    while not at_rest:
        try:
            grid[y_pos][x_pos]
            grid[y_pos + 1][x_pos]
            grid[y_pos][x_pos+1]
        except:
            return False

        if grid[y_pos + 1][x_pos] == ".":
            y_pos += 1
        elif grid[y_pos + 1][x_pos - 1] == ".":
            y_pos += 1
            x_pos -= 1
        elif grid[y_pos + 1][x_pos + 1] == ".":
            y_pos += 1
            x_pos += 1
        else:
            at_rest = True

    grid[y_pos][x_pos] = "O"

    return True # indicates sand came to rest as opposed to falling into the ether


def add_sand_p2(grid):
    y_pos, x_pos = 0, 500
    at_rest = False
    while not at_rest:
        if (x_pos + 1) >= len(grid[0]):
            for r in grid[:-1]:
                r.append(".")
            grid[-1].append("#")
        if grid[y_pos + 1][x_pos] == ".":
            y_pos += 1
        elif grid[y_pos + 1][x_pos - 1] == ".":
            y_pos += 1
            x_pos -= 1
        elif grid[y_pos + 1][x_pos + 1] == ".":
            y_pos += 1
            x_pos += 1
        else:
            at_rest = True

    grid[y_pos][x_pos] = "O"

    return True

def p1():
    g = make_grid()
    add_rock_to_grid(g)
    c = 0
    while add_sand(g):
         c += 1

    print("Part 1 -", c)


def p2():
    g = make_grid(p2 = True)
    add_rock_to_grid(g)

    c = 0
    while add_sand_p2(g):
        c += 1
        if g[0][500] == "O":
            break

    for l in g:
        print("".join(l))

    print("Part 2 - ", c)

if __name__ == "__main__":
    p1()
    p2()
