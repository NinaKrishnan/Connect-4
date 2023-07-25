from typing import List
from Game.GameToken.color import Color
from Game.Board.board import Board
from Game.Players.Human_Player.human_player import Human_Player



class Game:
    available_colors: List[Color] = list(Color)

    def __init__(self):
        available_colors = list(Color)
        self.board = Board()
        self.players = [Human_Player("Player 1"), Human_Player("Player 2")]


        



    def get_available_color(self) -> Color:
        if len(Game.available_colors) < 1:
            raise ValueError("No more colors available for new players.")
        
        
        return Game.available_colors.pop()
        





    def get_player_names(self):
        player_1 = 