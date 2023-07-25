from typing import List
import numpy as np
import Game.game
from Game.Board.board import Board
from Game.GameToken.game_token import GameToken
from Game.GameToken.color import Color



class Human_Player:
    
    def __init__(self, name: str):
        self.name = name
        self.tokens: List[GameToken] = self.generate_token_pool()



    def generate_token_pool(self, game: Game, n_tokens: int = 21) -> List[GameToken]:
        color: Color = game.get_available_color()
        token_stack: List[GameToken] = []

        for i in range(n_tokens):
            token_stack.append(GameToken(color))

        return token_stack


    def make_move(self, board: Board, col: int) -> Board:
        if col < 0 or col > board.cols -1:
            raise ValueError("Invalid column")

        for row in range(board.rows-1, -1, -1):
            if board[row][col] == None:
                board[row][col] = self.tokens.pop()

        return board
    







