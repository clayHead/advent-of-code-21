# There could be an error if the binary numbers are not all the same length. Gonna work on that
def error_checker(input):
    line = input.strip()
    as_set = set(line)
    base = {'0', '1'}

    if as_set == base or as_set == {'0'} or as_set == {'1'}:
        return True
    else:
        return False


def convert_binary_string(input):
    return int(input, 2)


# Most is a bool that when true we want to filter by most common, and least common when false
def filter_input(input, index, greatest):
    if len(input) == 1:
        return input[0]
    else:
        new_input = []
        zero = 0
        one = 0
        for line in input:
            if line[index] == '0':
                zero += 1
            else:
                one += 1
        if zero <= one:
            least = '0'
            most = '1'
        else:
            least = '1'
            most = '0'
        for line in input:
            if greatest and line[index] == most:
                new_input.append(line)
            elif not greatest and line[index] == least:
                new_input.append(line)
        index += 1
        return filter_input(new_input, index, greatest)


class HealthChecker:
    def __init__(self):
        self.gama = 0
        self.epsilon = 0
        self.oxygen = 0
        self.cO2 = 0
        self.input = []

        self.get_input()
        self.get_gama()
        self.get_epsilon()
        self.get_oxygen()
        self.get_cO2()

    def get_input(self):
        with open('../PuzzleInputs/d3-input', newline='') as f:
            lines = f.readlines()

            for line in lines:
                if not error_checker(line):
                    continue

                self.input.append(line.strip())

                # Gamma is a bool. When true we are getting the gama, false epsilon

    def string_from_input(self, gamma):
        greek_list = [0] * len(self.input[0])

        for x in range(len(self.input[0])):
            zero = 0
            one = 0

            for line in self.input:
                if line[x] == '0':
                    zero += 1
                else:
                    one += 1

            if zero <= one:
                least = '0'
                most = '1'
            else:
                least = '1'
                most = '0'

            if gamma:
                greek_list[x] = most
            else:
                greek_list[x] = least

        out_str = ""
        for symbol in greek_list:
            out_str += str(symbol)

        return out_str

    def get_gama(self):
        gamma_string = self.string_from_input(True)
        self.gama = convert_binary_string(gamma_string)

    def get_epsilon(self):
        epsilon_string = self.string_from_input(False)
        self.epsilon = convert_binary_string(epsilon_string)

    def get_oxygen(self):
        oxygen_string = filter_input(self.input, 0, True)
        self.oxygen = convert_binary_string(oxygen_string)

    def get_cO2(self):
        cO2_string = filter_input(self.input, 0, False)
        self.cO2 = convert_binary_string(cO2_string)

    def get_power_consumption(self):
        return self.gama * self.epsilon

    def get_lifesupport_rating(self):
        return self.oxygen * self.cO2


def main():
    checker = HealthChecker()
    print(checker.get_power_consumption())
    print(checker.get_lifesupport_rating())


if __name__ == "__main__":
    main()
