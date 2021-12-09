class Ray:
    def __init__(self, x1, y1, x2, y2):
        self.start = (x1, y1)
        self.end = (x2, y2)

    def print_ray(self):
        print("(", self.start[0], ",", self.start[1], ") -> (", self.end[0], ",", self.end[1], ")")

    def is_horizontal(self):
        if self.start[0] == self.end[0]:
            return True
        elif self.start[1] == self.end[1]:
            return False

    def is_vertical(self):
        if self.start[0] == self.end[0]:
            return False
        elif self.start[1] == self.end[1]:
            return True

    def get_middle_points(self):
        return_list = []
        if self.is_horizontal():
            y = self.start[1]
            if self.start[1] > self.end[1]:
                while y >= self.end[1]:
                    return_list.append((self.start[0], y))
                    y -= 1
            else:
                while y <= self.end[1]:
                    return_list.append((self.start[0], y))
                    y += 1
            return return_list
        elif self.is_vertical():
            x = self.start[0]
            if self.start[0] > self.end[0]:
                while x >= self.end[0]:
                    return_list.append((x, self.start[1]))
                    x -= 1
            else:
                while x <= self.end[0]:
                    return_list.append((x, self.start[1]))
                    x += 1
            return return_list
        else:
            # Diagonal
            x = self.start[0]
            y = self.start[1]
            x_go_down = self.start[0] > self.end[0]
            y_go_down = self.start[1] > self.end[1]

            while x != self.end[0] and y != self.end[1]:
                return_list.append((x, y))
                if x_go_down:
                    x -= 1
                else:
                    x += 1
                if y_go_down:
                    y -= 1
                else:
                    y += 1
            # Above list will miss last entry
            return_list.append((x, y))
            return return_list


class VentAnyalizer:
    def __init__(self):
        self.rays = []
        self.vent_field = {}

        self.get_input()

        self.find_vents()

    def get_input(self):
        with open('../PuzzleInputs/d5.in', newline='') as f:
            lines = f.readlines()

            for line in lines:
                if line.count("->") != 1:
                    print("ERROR! Key char not found")
                    continue
                split = line.split("->")
                left = split[0].strip()
                right = split[1].strip()

                l_ray_in = left.split(',')
                r_ray_in = right.split(',')

                try:
                    x1 = int(l_ray_in[0])
                    y1 = int(l_ray_in[1])
                    x2 = int(r_ray_in[0])
                    y2 = int(r_ray_in[1])
                except ValueError:
                    print("ERROR! Value is not an int")
                    continue

                ray = Ray(x1, y1, x2, y2)
                self.rays.append(ray)

    def find_vents(self):
        for ray in self.rays:
            points = ray.get_middle_points()
            for x in range(len(points)):
                if points[x] in self.vent_field.keys():
                    self.vent_field[points[x]] = self.vent_field[points[x]] + 1
                else:
                    self.vent_field[points[x]] = 1

    def get_num_overlaps(self):
        return_num = 0
        for key, value in self.vent_field.items():
            if value > 1:
                return_num += 1
        return return_num


def main():
    vent = VentAnyalizer()
    print(vent.get_num_overlaps())


if __name__ == "__main__":
    main()