from Game.game import Game
from Game.Board.board import Board
from Game.GameToken.game_token import GameToken
import mimetypes

def main():
   

   filename = "/frontend/connect4.js"
   mime_type, encoding = mimetypes.guess_type(filename)
   print(mime_type)


   


if __name__ == "__main__":
    main()

