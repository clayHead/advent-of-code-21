def error_check(input):
    if len(input) != 2:
        print("Illegal line! Line below:")
        print(*input, sep=", ")
        return False

    input[0] = input[0].strip()
    input[1] = input[1].strip()

    if not input[1].isnumeric():
        print("Instruction is not numeric! Instruction: " + input[1])
        return False

    return True


class SubController:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
        self.aim = 0
        self.instructions = []

        self.get_input()

    def get_input(self):
        with open('../PuzzleInputs/d2-input.csv', newline='') as f:
            lines = f.readlines()

            for line in lines:
                split = line.split(" ")

                if error_check(split):
                    split[1] = int(split[1])
                    self.instructions.append(split)

    def get_final_position(self):
        return self.depth * self.horizontal

    def process_instructions(self):
        for input in self.instructions:
            if input[0].lower() == 'forward':
                self.horizontal += input[1]
                self.depth = self.depth + (self.aim * input[1])
            elif input[0].lower() == 'down':
                self.aim += input[1]
            elif input[0].lower() == 'up':
                self.aim -= input[1]
            else:
                print("Illegal instruction! Instruction: " + input[0].lower())


def main():
    controller = SubController()
    controller.process_instructions()
    print(controller.get_final_position())


if __name__ == "__main__":
    main()
