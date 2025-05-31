class Player:
    def __init__(self, symbol, name=None):
        self.symbol = symbol  # 'X' or 'O'
        self.name = name or symbol

    def __str__(self):
        return self.name 