# Window settings
WINDOW_SIZE = 600
CELL_SIZE = WINDOW_SIZE // 3

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRID_COLOR = (50, 50, 50)
X_COLOR = (255, 50, 50)  # Red for X
O_COLOR = (50, 50, 255)  # Blue for O
TEXT_COLOR = (50, 200, 50)  # Green for text

# Line settings
LINE_WIDTH = 15
GRID_LINE_WIDTH = 2

# Game settings
WINNING_COMBINATIONS = [
    # Rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # Columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # Diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
] 