class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0

    def get_move(self):
        while True:
            try:
                move = input(
                    f"{self.name} ({self.symbol}), enter your move (row,col): "
                )

                row, col = move.strip().split(",")

                return int(row), int(col)

            except ValueError:
                print("Invalid input. Please enter row and column like '0,1'.")

    def add_score(self):
        self.score += 1

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_symbol(self):
        return self.symbol