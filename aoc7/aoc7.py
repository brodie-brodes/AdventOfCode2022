class Directory():

    def __init__(self, name):
        self.name = name
        self.child_dirs = []
        self.files = []

    def add_item(self, line_output):
        if line_output.startswith("dir"):
            dir_name = line_output.split(" ")[1]
            self.add_child_dir(dir_name)
        else:
            size = int(line_output.split(" ")[0])
            file_name = line_output.split(" ")[1]
            self.add_file(File(size, file_name))

    def add_child_dir(self, name):
        if not self.contains_dir(name):
            child = Directory(name)
            child.set_parent(self)
            self.child_dirs.append(child)

    def contains_dir(self, name):
        return any([d.name == name for d in self.child_dirs])

    def set_parent(self, directory):
        self.parent = directory

    def add_file(self, file):
        self.files.append(file)

    def get_dir(self, name):
        return [d for d in self.child_dirs if d.name == name][0]

    def get_size(self):
        size = sum([f.size for f in self.files])
        for child in self.child_dirs:
            size += child.get_size()

        return size

    def sum_children_under_size_s(self, s=100000):
        total = 0
        for child in self.child_dirs:
            total += child.sum_children_under_size_s(s)

        if self.get_size() <= s:
            total += self.get_size()

        return total

    def calc_min_viable_deletion(self, drive_size=70000000, space_required=30000000):
        unused_space = drive_size - self.get_size()
        min_viable_deletion_size = abs(space_required - unused_space)

        return min_viable_deletion_size

    def get_smallest_viable_deletion(self, min_viable_deletion_size):
        if self.get_size() < min_viable_deletion_size:
            return None

        viable_deletions = [self]
        for child in self.child_dirs:
            csvd = child.get_smallest_viable_deletion(min_viable_deletion_size)
            if csvd is not None:
                viable_deletions.append(csvd)

        return min(viable_deletions, key=lambda x: x.get_size())


class File():
    def __init__(self, size, name):
        self.name = name
        self.size = size


def build_tree_from_commands():
    master = Directory("/")
    for line in open("input.txt"):
        l = line.strip()
        if l == "$ cd /":
            working_dir = master
            continue
        if l == "$ ls":
            continue
        if l == "$ cd ..":
            working_dir = working_dir.parent
        elif l.startswith("$ cd "):
            change_dir = l.replace("$ cd ", "")
            working_dir = working_dir.get_dir(change_dir)
        if not l.startswith("$"):
            working_dir.add_item(l)

    return master


def main():
    tree = build_tree_from_commands()
    print("Total tree size - ", tree.get_size())
    print("Sum of sizes of directories under 10k - ", tree.sum_children_under_size_s())
    min_viable_deletion_size = tree.calc_min_viable_deletion()
    del_target = tree.get_smallest_viable_deletion(min_viable_deletion_size)
    print("Smallest viable directory to delete is {} with a size of {}".format(del_target.name, del_target.get_size()))


if __name__ == "__main__":
    main()