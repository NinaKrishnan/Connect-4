import numpy as np 
from enum import Enum


class GameToken:

    class Color(Enum):
        RED = 1
        YELLOW = 2


    def __init__(self, color):
        self.color = color