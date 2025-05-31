class AIPlayer:
    def __init__(self, symbol):
        self.symbol = symbol
        self.opponent_symbol = 'O' if symbol == 'X' else 'X'

    def get_best_move(self, board):
        best_score = float('-inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if board.grid[row][col] == '':
                    board.grid[row][col] = self.symbol
                    score = self.minimax(board, 0, False)
                    board.grid[row][col] = ''

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minimax(self, board, depth, is_maximizing):
        winner = board.check_winner()
        if winner == self.symbol:
            return 1
        elif winner == self.opponent_symbol:
            return -1
        elif board.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board.grid[row][col] == '':
                        board.grid[row][col] = self.symbol
                        score = self.minimax(board, depth + 1, False)
                        board.grid[row][col] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board.grid[row][col] == '':
                        board.grid[row][col] = self.opponent_symbol
                        score = self.minimax(board, depth + 1, True)
                        board.grid[row][col] = ''
                        best_score = min(score, best_score)
            return best_score 