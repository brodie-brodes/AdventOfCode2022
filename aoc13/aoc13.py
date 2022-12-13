from functools import cmp_to_key


def is_in_right_order(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return True, True # first boolean indicates whether solved, second is whether condition is true
        elif p1 > p2:
            return True, False
        else:
            return False, None # first boolean false in this case, instead move onto next element
    elif isinstance(p1, list) and isinstance(p2, int):
        p2 = [p2]
        return is_in_right_order(p1, p2)
    elif isinstance(p1, int) and isinstance(p2, list):
        p1 = [p1]
        return is_in_right_order(p1, p2)
    elif isinstance(p1, list) and isinstance(p2, list):
        max_idx = max([len(p1), len(p2)])
        for i in range(max_idx):
            if i >= len(p1) and i < len(p2):
                return True, True
            elif i < len(p1) and i >= len(p2):
                return True, False
            elif i >= len(p1) and i >= len(p2):
                return False, None
            p1_element, p2_element = p1[i], p2[i]
            result = is_in_right_order(p1_element, p2_element)
            if result[0]:
                return result

    return False, None


def compare_packets(p1, p2):
    if is_in_right_order(p1, p2)[1]:
        return -1
    else:
        return 1


def main():
    indices_true = []
    text = open("input.txt").read().strip()
    for idx, pair in enumerate(text.split("\n\n")):
        p1, p2 = [eval(p) for p in pair.split("\n")]
        if is_in_right_order(p1, p2)[1]:
            indices_true.append(idx + 1)

    packets = [eval(p) for p in text.split("\n") if p != ""]
    packets.append([[2]])
    packets.append([[6]])
    packets = sorted(packets, key=cmp_to_key(compare_packets))

    print("Part 1 - ", sum(indices_true))
    print("Part 2 - ", (packets.index([[2]]) + 1) * ((packets.index([[6]]) + 1)))


if __name__ == "__main__":
    main()