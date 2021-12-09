class CrabAligner:
    def __init__(self):
        self.positions = []
        self.fuel_spent = 0

        self.get_input()

    def get_input(self):
        with open('../PuzzleInputs/d7.in', newline='') as f:
            lines = f.readlines()

            strip = lines[0].strip()
            split = strip.split(',')

            for position in split:
                # Fairly simple error checking here
                if not position.isnumeric():
                    print("ERROR! Input in not numeric. Input:", position)
                    continue

                self.positions.append(int(position))

    # This was used for part 1
    def get_median(self):
        n = len(self.positions)
        s = sorted(self.positions)
        # TODO always return an int
        return (sum(s[n // 2 - 1:n // 2 + 1]) / 2.0, s[n // 2])[n % 2] if n else None

    def align_crabs(self):
        smallest = 9999999999999
        for target in range(max(self.positions)+1):
            spent = 0
            for position in self.positions:
                dif = abs(position - target)
                spent = spent + (dif * (dif + 1)/2)
            if spent <= smallest:
                smallest = spent
        self.fuel_spent = smallest
        print("Fuel spent", self.fuel_spent)


def main():
    aligner = CrabAligner()
    aligner.align_crabs()


if __name__ == "__main__":
    main()