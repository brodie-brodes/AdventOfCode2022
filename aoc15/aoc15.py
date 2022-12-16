class Sensor():
    def __init__(self, position):
        self.position = position

    def register_beacon(self, beacon):
        self.beacon = beacon
        self.distance_to_beacon = abs(self.position[0] - beacon.position[0]) + abs(self.position[1] - beacon.position[1])


    def fill_paths_to_y_line(self, positions_filled,  ypos=10):
        distance_to_y = abs(self.position[1] - ypos)
        if distance_to_y < self.distance_to_beacon:
            remaining_distance = self.distance_to_beacon - distance_to_y
            for xpos in range(self.position[0] - remaining_distance, self.position[0] + remaining_distance + 1):
                p = (xpos, ypos)
                if p not in positions_filled:
                    positions_filled[p] = ""

    def fill_paths_to_y_line2(self, ypos=10):
        distance_to_y = abs(self.position[1] - ypos)
        if distance_to_y < self.distance_to_beacon:
            remaining_distance = self.distance_to_beacon - distance_to_y
            return (self.position[0] - remaining_distance, self.position[0] + remaining_distance)


class Beacon():
    def __init__(self, position):
        self.position = position

class Position():
    def __init__(self, coords):
        self.coords = coords
        self.max_distance_called = 0


def covers_limit(r, limit):
    if not (r[0] <= 0 and r[1] >= limit):
        return False
    return True


def merge_ranges(ranges):
    for i in ranges:
        ranges_copy = ranges.copy()
        ranges_copy.remove(i)
        for j in ranges_copy:
            if (j[0] <=  i[0] <= j[1] + 1) or (j[0] <= i[1] <= j[1] + 1):
                new_min = min([i[0], j[0]])
                new_max = max([i[1], j[1]])
                ranges_copy.remove(j)
                ranges_copy.append((new_min, new_max))
                return ranges_copy, True

    return ranges, False


def merge_all_ranges(ranges):
    cont = True
    while cont:
        ranges, cont = merge_ranges(ranges)

    return ranges


def main():
    positions_filled = {}

    beacon_positions = []
    sensors = []
    for line in open("input.txt"):
        l = line.strip()
        sensor_coords = tuple([int(e) for e in l.split(":")[0].replace("Sensor at x=", "").split(", y=")])
        beacon_coords = tuple([int(e) for e in l.split("beacon is at x=")[1].split(", y=")])

        beacon_positions.append(beacon_coords)

        beacon = Beacon(beacon_coords)

        sensor = Sensor(sensor_coords)
        sensor.register_beacon(beacon)
        sensors.append(sensor)

    for sensor in sensors:
        sensor.fill_paths_to_y_line(positions_filled, 2000000)

    c = 0
    for k in positions_filled:
        if k not in beacon_positions:
            c += 1

    print("Part 1 - ", c)

    print("Running part 2 (takes ~40 seconds to run)")
    limit = 4000000
    for y in range(limit + 1):
        ranges = []
        for sensor in sensors:
            r = sensor.fill_paths_to_y_line2(ypos=y)
            if r is not None:
                ranges.append(r)

        ranges = merge_all_ranges(ranges)
        if not any([covers_limit(r, limit) for r in ranges]):
            print("Found at y = ", y)
            break
    print(ranges)
    print('Part 2 solution -', ((min(ranges)[1] + 1) * 4000000) + y)

if __name__ == "__main__":
    main()