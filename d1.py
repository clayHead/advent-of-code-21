def error_checker(input):
    line = input.strip()
    if not line.isnumeric():
        print("Input in not numeric! Input: " + line)
        return False
    return True


class DepthChecker:
    def __init__(self):
        self.sweepTotal = 0
        self.input = []

        self.get_input()

    def get_input(self):
        out = []

        with open('d1-input.csv', newline='') as f:
            lines = f.readlines()

            for line in lines:
                if not error_checker(line):
                    continue

                out.append(int(line))

        self.input = out

    def depth_checker_sum3(self):
        sum = prev_bigger = 0

        for x in range(len(self.input)):
            if x < 3:
                sum = sum + self.input[x]

            if x >= 3:
                old_sum = sum
                sum = sum + self.input[x] - self.input[x - 3]

                if sum > old_sum:
                    prev_bigger += 1

        self.sweepTotal = prev_bigger

    def depth_checker_simple(self):
        prev_bigger = 0

        for x in range(len(self.input)):
            if x == 1:
                continue

            if self.input[x] > self.input[x - 1]:
                prev_bigger += 1

        self.sweepTotal = prev_bigger

    def perform_check(self, simple):
        if simple:
            self.depth_checker_simple()
        else:
            self.depth_checker_sum3()


def main():
    checker = DepthChecker()
    checker.perform_check(False)
    print(checker.sweepTotal)


if __name__ == "__main__":
    main()
