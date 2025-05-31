import pygame
from .constants import *

class Board:
    def __init__(self):
        self.grid = [['' for _ in range(3)] for _ in range(3)]
        self.winner = None
        
    def make_move(self, row, col, player):
        if self.is_valid_move(row, col):
            self.grid[row][col] = player.symbol
            return True
        return False
    
    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.grid[row][col] == ''
    
    def check_winner(self):
        for combination in WINNING_COMBINATIONS:
            symbols = [self.grid[row][col] for row, col in combination]
            if len(set(symbols)) == 1 and symbols[0] != '':
                return symbols[0]
        return None
    
    def is_full(self):
        return all(self.grid[row][col] != '' for row in range(3) for col in range(3))
    
    def draw(self, screen):
        # Draw grid lines
        for i in range(1, 3):
            # Vertical lines
            pygame.draw.line(screen, GRID_COLOR,
                           (i * CELL_SIZE, 0),
                           (i * CELL_SIZE, WINDOW_SIZE),
                           GRID_LINE_WIDTH)
            # Horizontal lines
            pygame.draw.line(screen, GRID_COLOR,
                           (0, i * CELL_SIZE),
                           (WINDOW_SIZE, i * CELL_SIZE),
                           GRID_LINE_WIDTH)
        
        # Draw X's and O's
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == 'X':
                    self.draw_x(screen, row, col)
                elif self.grid[row][col] == 'O':
                    self.draw_o(screen, row, col)
    
    def draw_x(self, screen, row, col):
        padding = CELL_SIZE // 4
        x = col * CELL_SIZE
        y = row * CELL_SIZE
        
        pygame.draw.line(screen, X_COLOR,
                        (x + padding, y + padding),
                        (x + CELL_SIZE - padding, y + CELL_SIZE - padding),
                        LINE_WIDTH)
        pygame.draw.line(screen, X_COLOR,
                        (x + CELL_SIZE - padding, y + padding),
                        (x + padding, y + CELL_SIZE - padding),
                        LINE_WIDTH)
    
    def draw_o(self, screen, row, col):
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        
        pygame.draw.circle(screen, O_COLOR,
                         (x, y),
                         CELL_SIZE // 3,
                         LINE_WIDTH) 