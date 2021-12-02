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
                # Error Checker
                line = line.strip()
                if not line.isnumeric():
                    print("Input in not numeric! Input: " + line)
                    continue
                
                out.append(int(line))

        self.input = out

    def depth_checker_sum3(self):
        sum = old_sum = prevBigger = 0

        for x in range(len(self.input)):
            if x < 3:
                sum = sum + self.input[x]

            if x >= 3:
                old_sum = sum 
                sum = sum + self.input[x] - self.input[x-3]

                if sum > old_sum:
                    prevBigger += 1

        self.sweepTotal = prevBigger

    def depth_checker_simple(self):
        prevBigger = 0

        for x in range(len(self.input)):
            if x == 1:
                continue

            if self.input[x] > self.input[x-1]:
                prevBigger += 1

        self.sweepTotal = prevBigger

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