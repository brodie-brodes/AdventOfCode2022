def get_boxes():
    lines = [line.rstrip("\n") for line in open("input.txt") if not line.startswith("move")]
    cols = {}
    for idx, e in enumerate(lines[-2]):
        if e != " ":
            cols[e] = [line[idx] for line in lines[:-2] if len(line) > idx]
            cols[e] = [e for e in cols[e] if e != " "]

    return cols

def do_step_crate_mover_9000(boxes, moves):
    num_boxes = int(moves[0])
    src, dest = moves[1:]

    for move in range(num_boxes):
        box_to_move = boxes[src][0]

        boxes[src] = boxes[src][1:]
        boxes[dest] = [box_to_move] + boxes[dest]

def do_step_crate_mover_9001(boxes, moves):
    num_boxes = int(moves[0])
    src, dest = moves[1:]

    grab = boxes[src][:num_boxes]
    boxes[dest] = grab + boxes[dest]
    boxes[src] = boxes[src][num_boxes:]


def main():
    boxes_9000 = get_boxes()
    boxes_9001 = get_boxes()

    for line in open("input.txt"):
        l = line.strip()
        if l.startswith("move"):
            for w in ["move ", "from ", "to "]:
                l = l.replace(w, "")
            moves = l.split(" ")
            do_step_crate_mover_9000(boxes_9000, moves)
            do_step_crate_mover_9001(boxes_9001, moves)

    solution_9000 = "".join([boxes_9000[key][0] for key in boxes_9000])
    print("Solution for crate mover 9000 -", solution_9000)

    solution_9001 = "".join([boxes_9001[key][0] for key in boxes_9001])
    print("Solution for crate mover 9001 -", solution_9001)

if __name__ == "__main__":
    main()