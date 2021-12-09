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
        self.winning_draw = None
        self.end_val = 0

    def __str__(self):
        out = str(self.board[0])
        for x in range(5):
            if x == 0:
                continue
            out = out + "\n" + str(self.board[x])
        return out

    def append(self, line):
        self.board.append(line)

    def check_win(self, draw):
        for x in range(5):
            horz = 0
            for y in range(5):
                if self.board[x][y] == -1:
                    horz += 1
            if horz == 5:
                #print("Found a winner horz\n", self)
                self.winning_draw = draw
                self.get_final_score()
                return True
        for y in range(5):
            vert = 0
            for x in range(5):
                if self.board[x][y] == -1:
                    vert += 1
            if vert == 5:
                self.winning_draw = draw
                self.get_final_score()
                return True
        return False

    def check_draw(self, draw):
        for x in range(5):
            for y in range(5):
                if self.board[x][y] == draw:
                    self.board[x][y] = -1
                    return True

    def get_final_score(self):
        #print("Final board\n", self)
        total = 0
        for x in range(5):
            for y in range(5):
                if self.board[x][y] >= 0:
                    total += self.board[x][y]
        self.end_val = total * self.winning_draw


class BingoSystem:
    def __init__(self):
        self.boards = []
        self.draws = []

        self.winning_boards = []
        self.winning_draws = []
        self.win_vals = []

        self.already_won = []

        self.get_input()
        self.process_draws()

    def get_input(self):
        with open('../PuzzleInputs/d4.in', newline='') as f:
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
                    if len(line) == 5:
                        board.append(line)
                    elif x != 1:
                        # Don't count the first empty line
                        self.boards.append(board)
                        board = BingoBoard()
            self.boards.append(board)

            print(self.boards[0] == self.boards[0])

    def process_draws(self):
        # Go through each of the draws
        for draw in self.draws:
            # And update the entire set of boards
            if len(self.boards) == 0:
                print("No more boards! Draw:", draw)
                break
            for board in self.boards:
                # Don't process boards that have already won
                if board not in self.already_won:
                    board.check_draw(draw)

            # Check for and handle winners
            self.process_winners(draw)

            print("Remaining boards and amount of winners:", len(self.boards), len(self.winning_boards))

        # Process winners
        self.get_win_vals()

    def process_winners(self, draw):
        for board in self.boards:
            if board not in self.already_won and board.check_win(draw):
                print(board)
                self.already_won.append(board)
                board.winning_draw = draw
                self.winning_boards.append(board)
                self.boards.remove(board)

    def get_win_vals(self):
        for board in self.winning_boards:
            print(board.winning_draw, board.end_val)
            self.win_vals.append(board.end_val)


def main():
    bingo = BingoSystem()
    print("Num winners:", len(bingo.winning_boards))
    print("First and last vals", bingo.winning_boards[0].end_val, bingo.winning_boards[-1].end_val)


if __name__ == "__main__":
    main()
