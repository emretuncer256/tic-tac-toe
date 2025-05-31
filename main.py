import pygame
import sys
from game.board import Board
from game.player import Player
from game.ai_player import AIPlayer
from game.constants import *

class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Tic Tac Toe")
        
        self.board = Board()
        # Human is X (goes first), AI is O
        self.human = Player('X', "Human")
        self.computer = AIPlayer('O')
        self.current_player = 'human'  # Start with human
        self.game_over = False
        self.message = ""
        
        # Initialize font
        self.font = pygame.font.Font(None, 48)
        
        # Add timer for computer move
        self.computer_thinking = False
        self.computer_start_time = 0
        self.COMPUTER_THINK_TIME = 800  # milliseconds
    
    def make_computer_move(self):
        if not self.game_over:
            row, col = self.computer.get_best_move(self.board)
            self.board.grid[row][col] = self.computer.symbol
            
            winner = self.board.check_winner()
            if winner:
                self.message = "Computer wins!"
                self.game_over = True
            elif self.board.is_full():
                self.message = "It's a tie!"
                self.game_over = True
            else:
                self.current_player = 'human'
            
            self.computer_thinking = False
        
    def handle_click(self, pos):
        if self.game_over or self.current_player != 'human' or self.computer_thinking:
            return
            
        col = pos[0] // CELL_SIZE
        row = pos[1] // CELL_SIZE
        
        if self.board.is_valid_move(row, col):
            self.board.grid[row][col] = self.human.symbol
            
            winner = self.board.check_winner()
            if winner:
                self.message = "Human wins!"
                self.game_over = True
            elif self.board.is_full():
                self.message = "It's a tie!"
                self.game_over = True
            else:
                self.current_player = 'computer'
                self.computer_thinking = True
                self.computer_start_time = pygame.time.get_ticks()
    
    def draw_message(self):
        if self.message:
            text_surface = self.font.render(self.message, True, TEXT_COLOR)
            text_rect = text_surface.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
            background_rect = text_rect.inflate(20, 20)
            pygame.draw.rect(self.screen, (*WHITE, 200), background_rect)
            self.screen.blit(text_surface, text_rect)
        elif self.computer_thinking:
            text_surface = self.font.render("Computer is thinking...", True, TEXT_COLOR)
            text_rect = text_surface.get_rect(center=(WINDOW_SIZE // 2, 30))
            self.screen.blit(text_surface, text_rect)
    
    def run(self):
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60)  # Limit to 60 FPS
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.__init__()
            
            # Handle computer move after delay
            if self.computer_thinking:
                current_time = pygame.time.get_ticks()
                if current_time - self.computer_start_time >= self.COMPUTER_THINK_TIME:
                    self.make_computer_move()
            
            self.screen.fill(WHITE)
            self.board.draw(self.screen)
            self.draw_message()
            pygame.display.flip()

if __name__ == "__main__":
    game = TicTacToe()
    game.run() 