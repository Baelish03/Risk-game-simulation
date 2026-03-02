import numpy as np
from player import Player
import random

class Setup:
    def __init__(self, n_of_players, players):
        self.n_of_players = n_of_players
        self.players = players

    def initial_armies(self):
        """
        Assign initial armies to each player
        """
        n_of_players = self.n_of_players
        if n_of_players == 2:
            #pass
            raise ValueError(f"Number of players is 2") 
        elif 3 <= n_of_players <= 6:
            return 50 - 5 * n_of_players # armies follows this equation 
        else: 
            raise ValueError(f"Number of players is more than 6") 
        
    def players_order(self):
        """
        Decide what players' order
        """
        players = self.players
        random.shuffle(players)
        return players

POSSIBLE_PLAYERS = [Player("Alan", "red"), Player("Becca", "green"), Player("Charles", "blue"),
                    Player("Diane", "yellow"), Player("Emmanuel", "black"), Player("Fiona", "violet")] # better than player1, player2, etc...
N_OF_PLAYERS = 6
PLAYERS = POSSIBLE_PLAYERS[:N_OF_PLAYERS] # select a subset from possible players with number of players dimension

setup = Setup(N_OF_PLAYERS, PLAYERS)
for player in PLAYERS:
    player.armies_available = setup.initial_armies()

ordered_players = setup.players_order()

print(PLAYERS)




