# Tic Tac Toe with Minimax AI

A Python implementation of the classic Tic Tac Toe game with an AI opponent using the Minimax algorithm. The game features a graphical user interface built with Pygame.

## Features

- Interactive GUI using Pygame
- Human vs AI gameplay
- AI opponent using the Minimax algorithm for optimal moves
- Visual feedback for game state
- Restart game functionality

## Requirements

- Python 3.x
- Pygame 2.6.1

## Installation

1. Clone the repository:
```bash
git clone https://github.com/emretuncer256/tic-tac-toe.git
cd TicTacToe
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## How to Play

1. Run the game:
```bash
python main.py
```

2. Game Rules:
   - You play as 'X' and the computer plays as 'O'
   - Click on any empty cell to make your move
   - The computer will automatically make its move after a short delay
   - Press 'R' key to restart the game at any time

## Project Structure

```
TicTacToe/
├── main.py              # Main game loop and GUI implementation
├── game/
│   ├── board.py        # Board class for game state management
│   ├── player.py       # Player class for human player
│   ├── ai_player.py    # AI player implementation with Minimax
│   └── constants.py    # Game constants and configurations
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Implementation Details

The AI opponent uses the Minimax algorithm to determine the optimal move. The algorithm:
- Evaluates all possible moves
- Simulates future game states
- Chooses the move that maximizes its chances of winning
- Implements alpha-beta pruning for efficiency

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Pygame library for the game interface
- Minimax algorithm for AI implementation 