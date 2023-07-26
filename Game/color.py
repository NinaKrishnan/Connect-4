from enum import Enum
from Game.GameToken.game_token import GameToken

class Color(Enum):
    RED = "R"
    YELLOW = "Y"
    


    @staticmethod
    def to_string(token: GameToken) -> str:
        token_to_string = {
            None: "-",
            GameToken(Color.RED): Color.RED.value,
            GameToken(Color.YELLOW): Color.YELLOW.value
        }

        return token_to_string[token]

    
    