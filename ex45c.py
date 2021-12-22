# from sys import exit
# import time
# import sys
# from random import randint
from ex45a import * # Engine
# from ex45b import *
from ex45nice import *

a_map = Map('central_kingdom')
a_game = Engine(a_map)
a_game.play()