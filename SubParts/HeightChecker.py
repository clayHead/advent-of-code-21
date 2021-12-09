class HeightChecker:
    def __init__(self):
        self.height_map = []        # List of lists
        self.lowest_points = []     # List of tuples
        self.basins = []            # List of lists of tuples

        # TODO Maybe other parts can use a similar check as below?
        # I.e input is so bad, code won't work
        if self.get_input():
            self.find_lowest_points()

    def get_input(self):
        with open('../PuzzleInputs/d9.in', newline='') as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip()
                num_list = []
                for num in line:
                    try:
                        num_list.append(int(num))
                    except ValueError:
                        print("Input is not numerical!")
                self.height_map.append(num_list)

            length = len(self.height_map[0])
            for h_map in self.height_map:
                if len(h_map) != length:
                    print("ERROR! The whole thing is borked! Try an input with the same amount of nums on a line!")
                    return False
        return True

    def check_bounds(self, x, y):
        y_upper_in_bounds = (y + 1 < len(self.height_map[0]))
        y_lower_in_bounds = (len(self.height_map[0]) > y - 1 >= 0)
        x_upper_in_bounds = (x + 1 < len(self.height_map))
        x_lower_in_bounds = (len(self.height_map) > x - 1 >= 0)

        return y_upper_in_bounds, y_lower_in_bounds, x_upper_in_bounds, x_lower_in_bounds

    def find_lowest_points(self):
        for x in range(len(self.height_map)):
            for y in range(len(self.height_map[0])):
                # 0 is always a low point and 9 is never, short circuit
                if self.height_map[x][y] == 0:
                    self.lowest_points.append((x, y))
                    continue
                elif self.height_map[x][y] == 9:
                    continue

                # Check bounds
                bound_check = self.check_bounds(x, y)
                y_upper_in_bounds = bound_check[0]
                y_lower_in_bounds = bound_check[1]
                x_upper_in_bounds = bound_check[2]
                x_lower_in_bounds = bound_check[3]

                if y_upper_in_bounds:
                    if self.height_map[x][y] > self.height_map[x][y+1]:
                        # Found a bigger value
                        continue
                if y_lower_in_bounds:
                    if self.height_map[x][y] > self.height_map[x][y-1]:
                        # Found a bigger value
                        continue
                if x_upper_in_bounds:
                    if self.height_map[x][y] > self.height_map[x+1][y]:
                        # Found a bigger value
                        continue
                if x_lower_in_bounds:
                    if self.height_map[x][y] > self.height_map[x-1][y]:
                        # Found a bigger value
                        continue
                # If all these checks fail, then there are no adjacent spaces that are lower
                self.lowest_points.append((x, y))

        # Get all basins
        for point in self.lowest_points:
            self.basins.append(self.find_basin([point]))

    def find_basin(self, basin):
        for low_p in basin:
            # Check bounds
            bound_check = self.check_bounds(low_p[0], low_p[1])
            y_upper_in_bounds = bound_check[0]
            y_lower_in_bounds = bound_check[1]
            x_upper_in_bounds = bound_check[2]
            x_lower_in_bounds = bound_check[3]

            if y_upper_in_bounds:
                if (low_p[0], low_p[1]+1) not in basin and self.height_map[low_p[0]][low_p[1]+1] != 9:
                    basin.append((low_p[0], low_p[1]+1))
            if y_lower_in_bounds:
                if (low_p[0], low_p[1]-1) not in basin and self.height_map[low_p[0]][low_p[1]-1] != 9:
                    basin.append((low_p[0], low_p[1]-1))
            if x_upper_in_bounds:
                if (low_p[0]+1, low_p[1]) not in basin and self.height_map[low_p[0]+1][low_p[1]] != 9:
                    basin.append((low_p[0]+1, low_p[1]))
            if x_lower_in_bounds:
                if (low_p[0]-1, low_p[1]) not in basin and self.height_map[low_p[0]-1][low_p[1]] != 9:
                    basin.append((low_p[0]-1, low_p[1]))
        return basin

    def get_risk_sum(self):
        sum = 0
        for point in self.lowest_points:
            sum += self.height_map[point[0]][point[1]] + 1
        return sum

    def get_basin_total(self):
        # There is probably a more elegant way to do this, but it works
        self.basins.sort(key=len)
        self.basins.reverse()
        if len(self.basins) < 3:
            print("ERROR! There weren't 3 basins")
            return None
        return len(self.basins[0]) * len(self.basins[1]) * len(self.basins[2])


def main():
    checker = HeightChecker()
    print(checker.get_risk_sum())
    print(checker.get_basin_total())


if __name__ == "__main__":
    main()