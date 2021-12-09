def error_checker(to_check, length):
    if len(to_check) > length:
        print("num args to much. Got:", len(to_check), "Expecting less than:", length)
        return False
    for val in to_check:
        if len(val) > 7:
            print(val, "is too long")
            return False
        for digit in val:
            if digit >= 'h':
                print(digit, "in", val, "is too big")
                return False
    return True


class DisplayChecker:
    def __init__(self):
        self.signal_patterns = []
        self.output_values = []
        self.decoded_signal = []
        self.decoded_output = []

        self.get_input()

    def get_input(self):
        with open('../PuzzleInputs/d8.in', newline='') as f:
            lines = f.readlines()

            for line in lines:
                # Sanitize and check for key character
                line = line.strip()
                if line.count("|") != 1:
                    print("ERROR! No '|' char found")
                    continue

                split = line.split(" | ")
                left = split[0].split(" ")
                right = split[1].split(" ")

                # Check both sides
                if not error_checker(left, 10):
                    print("ERROR!")
                    continue
                if not error_checker(right, 5):
                    print("ERROR!")
                    continue

                self.signal_patterns.append(left)
                self.output_values.append(right)

    def map_unique(self, entry):
        if len(entry) == 2:
            return '1'
        elif len(entry) == 3:
            return '7'
        elif len(entry) == 4:
            return '4'
        elif len(entry) == 7:
            return '8'
        else:
            return None

    def unique_outputs(self):
        num = 0
        for output in self.output_values:
            for entry in output:
                if self.map_unique(entry) is not None:
                    num += 1
        return num

    def decode_outputs(self):
        for i in range(len(self.signal_patterns)):
            result = self.decode_digits(i)
            self.decoded_output.append(result)

    def decode_digits(self, index):
        full_digit = []

        # build dict for values used for deciphering
        # We know the certain values above have unique lens
        # So if we see one of these unique ones, we know its mapping
        cipher = {}
        for val in self.signal_patterns[index]:
            if len(val) == 2:
                cipher[1] = val
            elif len(val) == 4:
                cipher[4] = val
            elif len(val) == 3:
                cipher[7] = val
            elif len(val) == 7:
                cipher[8] = val
            else:
                continue

        i = 0
        for digit in self.output_values[index]:
            v = self.map_unique(digit)
            if v is None:
                if len(digit) == 5:
                    v = self.decode_five_digit(cipher, digit)
                elif len(digit) == 6:
                    v = self.decode_six_digit(cipher, digit)
            full_digit.append(v)

        total = ''
        for digit in full_digit:
            total += digit
        return int(total)

    def decode_five_digit(self, cipher, value):
        in_four = 0
        in_one = 0
        for i in value:
            if i in cipher[4]:
                in_four += 1
            if i in cipher[1]:
                in_one += 1
        if in_four == 2:
            return '2'
        elif in_one == 2:
            return '3'
        else:
            return '5'

    def decode_six_digit(self, cipher, value):
        in_four = 0
        in_one = 0
        for i in value:
            if i in cipher[4]:
                in_four += 1
            if i in cipher[1]:
                in_one += 1
        if in_one == 1:
            return '6'
        elif in_four == 4:
            return '9'
        else:
            return '0'

    def sum_outputs(self):
        sum = 0
        for val in self.decoded_output:
            sum += val
        return sum


def main():
    checker = DisplayChecker()
    num_unique = checker.unique_outputs()
    checker.decode_outputs()
    sum = checker.sum_outputs()
    print(num_unique, sum)


if __name__ == "__main__":
    main()