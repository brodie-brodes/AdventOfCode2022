class CycleState():

    ADDX_CYCLE_THRESHOLD = 1

    def __init__(self, commands, init_signal_strength=1):

        self.signal_strength = init_signal_strength
        self.commands = commands

        self.cycle_num = 1
        self.command_num = 0
        self.addx_timer = 0
        self.screen_display = []


    def do_cycle(self):
        if (self.cycle_num - 1) % 40 == 0:
            self.screen_display.append([])
        self.draw_pixel()
        self.do_current_command()
        self.cycle_num += 1


    def show_screen_display(self):
        for l in self.screen_display:
            print("".join(l))


    def do_current_command(self):
        command = self.commands[self.command_num]
        if command == "noop":
            self.command_num += 1
        if command.startswith("addx"):
            if self.addx_timer == CycleState.ADDX_CYCLE_THRESHOLD:
                x_val = int(command.split(" ")[1])
                self.signal_strength += x_val
                self.command_num += 1
                self.addx_timer = 0
            else:
                self.addx_timer += 1


    def draw_pixel(self):
        visible = False
        ppos = (self.cycle_num - 1) % 40
        if self.signal_strength - 1 <= ppos <= self.signal_strength + 1:
            visible = True

        self.screen_display[-1].append("#" if visible else ".")

def main():
    commands = [i.strip() for i in open("input.txt")]
    cs = CycleState(commands)
    signal_sum = 0
    for i in range(240):
        cs.do_cycle()
        if cs.cycle_num in [20, 60, 100, 140, 180, 220]:
            signal_sum += cs.cycle_num * cs.signal_strength

    print("Signal sum (part 1):", signal_sum)
    cs.show_screen_display()


if __name__ == "__main__":
    main()