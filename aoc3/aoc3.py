def get_compartments(rucksack):
    rucksack = rucksack.strip()
    halfway = int(len(rucksack) / 2)
    return rucksack[:halfway], rucksack[halfway:]

def get_common_item(c1, c2):
    s1 = set(list(c1))
    s2 = set(list(c2))

    return list(s1.intersection(s2))[0]

def get_item_priority(item):
    letters = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters.index(item)

def get_badge(group):
    s1, s2, s3 = [set(e) for e in group]

    return list(s1.intersection(s2, s3))[0]

def main():
    total = 0
    group = []
    total_badges = 0
    for rucksack in open("input.txt"):
        print(group)
        c1, c2 = get_compartments(rucksack)
        item = get_common_item(c1, c2)
        total += get_item_priority(item)

        if len(group) < 3:
            group.append(rucksack.strip())


        if len(group) == 3:
            badge = get_badge(group)
            total_badges += get_item_priority(badge)
            group = []

    return total, total_badges

print(main())