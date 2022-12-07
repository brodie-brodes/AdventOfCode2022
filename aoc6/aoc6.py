def has_dupes(ss):
    for char in ss:
        if list(ss).count(char) > 1:
            return True

    return False

def get_index_first_marker(s):
    idx = 14
    while True:
        if not has_dupes(s[idx - 14: idx]):
            return idx
        idx += 1


def main():
    with open("input.txt") as f:
        s = f.read().strip()

    print(get_index_first_marker(s))

if __name__ == "__main__":
    main()