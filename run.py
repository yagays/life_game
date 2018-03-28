import numpy as np
from life_game import LifeGame

lg = LifeGame(40, 60)
lg.max_generation = 1000

lg.random()
# lg.add_glider(5,5)

lg.run()
