class Board:
    def __init__(self, size=20):
        self.size = size
        self.board = {(i, j): 0 for i in range(self.size) for j in range(self.size)}

    def add_mark(self, pos, player):
        self.board[pos] = player

