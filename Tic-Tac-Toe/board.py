class Board:
    def __init__(self):
        self.width = 3
        self.height = 3
        self.grid = self.create_empty_grid()

    def create_empty_grid(self):
        grid = []

        for row in range(self.height):
            new_row = []

            for col in range(self.width):
                new_row.append(" ")

            grid.append(new_row)

        return grid

    def __str__(self):
        board_string = ""

        for row_index in range(self.height):
            row_string = " " + " | ".join(self.grid[row_index]) + " \n"
            board_string += row_string

            if row_index < self.height - 1:
                separator = "---+" * (self.width - 1) + "---\n"
                board_string += separator

        return board_string

    def make_move(self, row, col, symbol):
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            return False

        if self.grid[row][col] != " ":
            return False

        self.grid[row][col] = symbol
        return True

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == " ":
                    return False

        return True

    def check_winner(self, symbol):
        # Rows
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True

        # Columns
        for col in range(3):
            if all(self.grid[row][col] == symbol for row in range(3)):
                return True

        # Diagonals
        if all(self.grid[i][i] == symbol for i in range(3)):
            return True

        if all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True

        return False

    def reset(self):
        self.grid = self.create_empty_grid()