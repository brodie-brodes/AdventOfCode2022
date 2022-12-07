class Elf():

    def __init__(self, items):
        self.items = items

    def get_cal_total(self):
        return sum([item.cals for item in self.items])


class Item():
    def __init__(self, cals):
        self.cals = cals


class ElfGroup():
    def __init__(self, info_string):
        self.elves = []
        for elf_info in info_string.strip().split("\n\n"):
            items = [Item(int(c)) for c in elf_info.split("\n")]
            self.elves.append(Elf(items))

    def get_max_cal_total(self):
        return max([e.get_cal_total() for e in self.elves])

    def get_top3_total(self):
        l = self.elves.copy()
        l.sort(key=lambda x: x.get_cal_total())

        return sum([e.get_cal_total() for e in l[-3:]])

def main():
    with open("input.txt") as f:
        s = f.read()

    eg = ElfGroup(s)
    print(eg.get_max_cal_total())
    print(eg.get_top3_total())

if __name__ == "__main__":
    main()