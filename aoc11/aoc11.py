import math

class MonkeyTroop():

    def __init__(self):
        self.monkeys = get_monkeys(self)
        self.worry_level_product = math.prod([self.monkeys[m].test for m in self.monkeys])

    def do_round(self, p2=False):
        for m in self.monkeys:
            self.monkeys[m].do_turn(p2=p2)

    def get_level_monkey_business(self):
        vals = [self.monkeys[k].items_inspected for k in self.monkeys]
        vals.sort()
        return vals[-2] * vals[-1]


class Monkey():

    def __init__(self, monkey_id, starting_items, operation, test, action_if_true, action_if_false, troop):
        self.id = monkey_id
        self.items = [Item(i, troop) for i in starting_items]
        self.operation = operation
        self.test = test
        self.action_if_true = action_if_true
        self.action_if_false = action_if_false
        self.troop = troop
        self.items_inspected = 0

    def do_turn(self, p2=False):
        items = self.items.copy()
        for item in items:
            self.inspect(item)
            if p2:
                item.mod_worry()
            else:
                self.get_bored(item)
            self.throw_item(item)

    def inspect(self, item):
        item.do_operation(self.operation)
        self.items_inspected += 1

    def get_bored(self, item):
        item.reduce_worry()

    def throw_item(self, item):
        if item.worry_level % self.test == 0:
            recipient_monkey = self.action_if_true
        else:
            recipient_monkey = self.action_if_false

        self.items.remove(item)
        self.troop.monkeys[recipient_monkey].add_item(item)

    def add_item(self, item):
        self.items.append(item)



class Item():
    def __init__(self, worry_level, troop):
        self.worry_level = worry_level
        self.factors = []
        self.troop = troop

    def do_operation(self, operation):
        operator, coef = operation.split(" ")
        if coef == "old":
            coef = self.worry_level
        if operator == "*":
            self.worry_level *= int(coef)
        elif operator == "+":
            self.worry_level += int(coef)

    def reduce_worry(self):
        self.worry_level = math.floor(self.worry_level / 3)

    def mod_worry(self):
        self.worry_level %= self.troop.worry_level_product


def get_monkeys(monkey_troop):
    monkeys = {}
    input_text = open("input.txt").read().strip().split("\n\n")
    for m in input_text:
        m = m.split("\n")
        monkey_id = int(m[0].split(" ")[1].rstrip(":"))
        items = [int(i) for i in m[1].replace("  Starting items: ", "").split(",")]
        operation = m[2].replace("  Operation: new = old ", "")
        test = int(m[3].replace("  Test: divisible by ", ""))
        action_if_true = int(m[4].replace("    If true: throw to monkey ", ""))
        action_if_false = int(m[5].replace("    If false: throw to monkey ", ""))

        monkey = Monkey(monkey_id, items, operation, test, action_if_true, action_if_false, troop=monkey_troop)
        monkeys[monkey_id] = monkey

    return monkeys


def p1():
    troop = MonkeyTroop()
    for r in range(20):
        troop.do_round()

    print("Monkey business level after 20 rounds (p1) - {}".format(troop.get_level_monkey_business()))

def p2():
    troop = MonkeyTroop()

    for r in range(10000):
        troop.do_round(p2=True)

    print("Monkey business level after 10000 rounds (p2) - {}".format(troop.get_level_monkey_business()))

if __name__ == "__main__":
    p1()
    p2()