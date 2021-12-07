def is_list_of_nums(input):
    out_list = []
    for i in input:
        try:
            out_list.append(int(i))
        except ValueError:
            continue
    return out_list


class BingoBoard:
    def __init__(self):
        self.board = []  # List of Lists

    def __str__(self):
        out = ""
        for line in self.board:
            out = out + str(line)
        return out

    def append(self, line):
        self.board.append(line)

    def get_board(self):
        return self.board

    def get_line(self, line):
        if line <= 4:
            return self.board[line]


class BingoSystem:
    def __init__(self):
        self.boards = []
        self.draws = []

        self.winning_board = BingoBoard()
        self.winning_draw = 0
        self.highestScore = 0

        self.already_won = []

        self.losing_board = BingoBoard()
        self.num_wins = 0
        self.last_draw = 0
        self.lowest_score = 0

        self.get_input()
        self.process_draws()

    def get_input(self):
        with open('../TestInputs/d4.test', newline='') as f:
            lines = f.readlines()

            # TODO Missing Error check for length of bingo board
            board = BingoBoard()
            for x in range(len(lines)):
                temp = lines[x].strip().split(' ')
                if x == 0:
                    # Get input from line
                    temp = lines[x].strip().split(',')
                    self.draws = is_list_of_nums(temp)
                else:
                    line = is_list_of_nums(temp)
                    if len(line) > 0:
                        board.append(line)
                    elif x != 1:
                        # Don't count the first empty line
                        self.boards.append(board)
                        board = BingoBoard()
            self.boards.append(board)

    def pos_in_board(self, index, draw):
        # Index is the index of the board to process
        board = self.boards[index].get_board()
        for x in range(5):
            line = board[x]
            for y in range(5):
                if line[y] == draw:
                    return x, y
        return None

    def process_draws(self):
        winning_draws = []
        for val in self.draws:
            # Update Board
            for x in range(len(self.boards)):
                pos = self.pos_in_board(x, val)
                if pos is not None:
                    self.boards[x].get_board()[pos[0]][pos[1]] = -1

            # Check for win
            result = self.check_for_winner()

            # Handle win
            if result.get('Result'):
                self.num_wins = self.num_wins + 1
                print(self.already_won)
                winning_draws.append(val)
                if self.num_wins == 1:
                    print("Winner", self.boards[result.get('Winner')])
                    self.winning_draw = val
                    self.winning_board = self.boards[result.get('Winner')].get_board()
                    self.get_win_val()

        # Handle last win
        print("How many winners", len(self.already_won))
        self.last_draw = winning_draws[-1]
        print("self.last_draw", self.last_draw)

        print("Last Winner", self.already_won[-1])
        self.losing_board = self.boards[self.already_won[-1]].get_board()
        print(self.losing_board)
        self.get_lose_val()
        print("end of process")

    def check_for_winner(self):
        return_dict = dict()
        for x in range(len(self.boards)):
            board = self.boards[x].get_board()
            for y in range(5):
                if board[y].count(-1) == 5 and x not in self.already_won:
                    print("Horz winner", x)
                    self.already_won.append(x)
                    return_dict['Result'] = True
                    return_dict['Winner'] = x
                    return return_dict
                else:
                    num_seen = 0
                    for z in range(5):
                        if board[y][z] == -1:
                            num_seen += 1
                    if num_seen == 5 and x not in self.already_won:
                        print("Vert winner", x)
                        self.already_won.append(x)
                        return_dict['Result'] = True
                        return_dict['Winner'] = x
                        return return_dict

        return_dict['Result'] = False
        return_dict['Winner'] = -1
        return return_dict

    def get_win_val(self):
        sum = 0
        for x in range(5):
            line = self.winning_board[x]
            for val in line:
                if val >= 0:
                    sum += val
        self.highestScore = sum * self.winning_draw

    def get_lose_val(self):
        sum = 0
        for x in range(5):
            line = self.losing_board[x]
            for val in line:
                if val >= 0:
                    sum += val
        print("sum and last draw", sum, self.last_draw)
        self.lowest_score = sum * self.last_draw


def main():
    bingo = BingoSystem()
    print(bingo.highestScore)
    print(bingo.lowest_score)


if __name__ == "__main__":
    main()
