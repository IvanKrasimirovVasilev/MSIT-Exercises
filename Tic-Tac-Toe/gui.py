import tkinter as tk


class Gui:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2

        self.current_player = player1

        # Create window
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        # Show current player / winner
        self.message = tk.Label(
            self.window,
            text=f"{self.current_player.get_name()}'s turn",
            font=("Arial", 16)
        )
        self.message.grid(row=0, column=0, columnspan=3)

        # Create buttons
        self.buttons = []

        for row in range(3):
            button_row = []

            for col in range(3):
                button = tk.Button(
                    self.window,
                    text=" ",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )

                button.grid(row=row + 1, column=col)
                button_row.append(button)

            self.buttons.append(button_row)

        # Score
        self.score_label = tk.Label(
            self.window,
            text=self.get_score_text(),
            font=("Arial", 14)
        )
        self.score_label.grid(row=4, column=0, columnspan=3)

        # New Game button
        self.new_game_button = tk.Button(
            self.window,
            text="New Game",
            command=self.new_game
        )
        self.new_game_button.grid(row=5, column=0, columnspan=3)

    def make_move(self, row, col):

        symbol = self.current_player.get_symbol()

        if self.board.make_move(row, col, symbol):

            # Show X or O
            self.buttons[row][col]["text"] = symbol
            self.buttons[row][col]["state"] = "disabled"

            # Winner?
            if self.board.check_winner(symbol):
                self.message["text"] = (
                    f"{self.current_player.get_name()} wins!"
                )

                self.current_player.add_score()

                self.score_label["text"] = self.get_score_text()

                self.disable_buttons()
                return

            # Draw?
            if self.board.is_full():
                self.message["text"] = "It's a draw!"
                return

            # Switch player
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1

            self.message["text"] = (
                f"{self.current_player.get_name()}'s turn"
            )

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button["state"] = "disabled"

    def get_score_text(self):
        return (
            f"{self.player1.get_name()} "
            f"{self.player1.get_score()} : "
            f"{self.player2.get_score()} "
            f"{self.player2.get_name()}"
        )

    def new_game(self):
        self.board.reset()

        self.current_player = self.player1

        self.message["text"] = (
            f"{self.current_player.get_name()}'s turn"
        )

        for row in self.buttons:
            for button in row:
                button["text"] = " "
                button["state"] = "normal"

    def run(self):
        self.window.mainloop()