from board import Board
from player import Player
from gui import Gui


player1 = Player("Ivan", "X")
player2 = Player("Toni", "O")

board = Board()

gui = Gui(board, player1, player2)

gui.run()