# This class was used for the solution to part 1. It was not used for part 2 as it was too slow
# If the fish did not live forever, it could still be used to model such behavior
class Fish:
    def __init__(self, age):
        self.age = age

    def print_fish(self):
        print("This fish is", self.age, "days old")

    def next_day(self):
        if self.age == 0:
            self.age = 6
            return Fish(8)
        else:
            self.age -= 1


class FishTracker:
    def __init__(self):
        self.fish = []
        self.stats = [0] * 9  # How many fish are that old

        self.get_input()

    def get_input(self):
        with open('../PuzzleInputs/d6-input', newline='') as f:
            lines = f.readlines()

            # TODO Error Checker
            strip = lines[0].strip()
            split = strip.split(',')

            for age in split:
                self.fish.append(Fish(int(age)))
                self.stats[int(age)] += 1

    def process_days(self, days):
        for x in range(days):
            self.process_day()

        print("There are", sum(self.stats), "fishes after", days, "days")

    def process_day(self):
        new_fish = self.stats[0]
        self.stats = self.stats[1:] + [self.stats[0]]
        self.stats[6] += new_fish


def main():
    tracker = FishTracker()
    tracker.process_days(256)


if __name__ == "__main__":
    main()