from enum import Enum
from typing import List


class GameToken:

    class Color(Enum):
        RED = "R"
        YELLOW = "Y"
        BLUE = "B"
        GREEN = "G"
        


    available_colors: List[Color] = list(Color)


    def __init__(self, color: Color):
        self.color = color

   

    def color_to_string(self) -> str:
        pass


    @classmethod
    def get_available_colors(cls) -> Color:
        return cls.available_colors.pop()

    @classmethod
    def reset_colors(cls):
        cls.available_colors = list(cls.Color)
        


  
    

