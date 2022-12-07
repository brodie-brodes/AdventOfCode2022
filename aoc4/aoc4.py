def get_pairs():
    for line in open("input.txt"):
        r1, r2 = line.strip().split(",")
        r1 = [int(i) for i in r1.split("-")]
        r2 = [int(i) for i in r2.split("-")]
        yield r1, r2

def is_fully_contained(r1, r2):
    if r1[0] > r2[0]:
        return False
    if r1[1] < r2[1]:
        return False
    return True

def is_overlapping(r1, r2):
    if r2[0] <= r1[0] <= r2[1]:
        return True
    if r2[0] <= r1[1] <= r2[1]:
        return True
    return False

def main():
    fully_contained_pairs = 0
    overlapping_pairs = 0
    for r1, r2 in get_pairs():
        if is_fully_contained(r1, r2) or is_fully_contained(r2, r1):
            fully_contained_pairs += 1
        if is_overlapping(r1, r2) or is_overlapping(r2, r1):
            overlapping_pairs += 1

    print("Total fully contained pairs -", fully_contained_pairs)
    print("Total overlapping pairs -", overlapping_pairs)

if __name__ == "__main__":
    main()