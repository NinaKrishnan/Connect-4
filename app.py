#REST API - main entry point
from flask import Flask, jsonify, request
import numpy as np

from Game.Board.board import Board
from Game.Players.Human_Player.human_player import Human_Player
from Game.game import Game
from Game.GameToken.game_token import GameToken
from Game.color import Color




app = Flask(__name__)