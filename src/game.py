class Game:
    def __init__(self, board):
        self.board = board
        self.moves_to_check # coordinate : value
        self.last_move = None

    def find_best_move(self):
        pass

    def evaluate_board(self):
        pass

    def check_winner(self, last_move):
        pass


    def minimax(self, node, depth, alpha, beta, isMaximizer):
        if depth == 0:
            return node
        
        if isMaximizer:
            max_value = float('-inf')

            for next_node in self.moves_to_check:
                value = self.minimax(next_node, depth - 1, alpha, beta, False)
                max_value = max(max_value, value)
                alpha = max(alpha, value)

                if beta <= alpha:
                    break

            return max_value
        
        else:
            min_value = float('inf')

            for next_node in self.moves_to_check:
                value = self.minimax(next_node, depth - 1, alpha, beta, True)
                min_value = min(min_value, value)
                alpha = max(alpha, value)

                if beta <= alpha:
                    break

            return min_value

