import random

class Setup:
    def __init__(self, n_of_players, players):
        self.n_of_players = n_of_players
        self.players = players
        
    def players_order(self):
        """
        Decide what players' order
        """
        players = self.players[:]
        random.shuffle(players)
        return players
    
    def has_free_territories(self, graph):
        return any(attr["owner"] == "NonePlayer"
                for _, attr in graph.nodes(data=True))
    
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
        
    def strategy_initial_territory(self, graph):
        """
        First try, simple strategy, RANDOM
        """
        free_node = [node for node, attributes in graph.nodes(data=True) if attributes['owner']=="NonePlayer"]
        return random.choice(free_node)
    
    def assign_initial_territory(self, graph, country, player):
        """
        Assign a single territory.
        For now this funtion is for the initial assignation, but maybe it can be usefu in general.
        """
        graph.nodes[country]["owner"] = player.name
        graph.nodes[country]["armies"] = 1
        graph.nodes[country]["label_color"] = player.color
        player.territories.add(country)
        player.armies_available -=1
        return graph, player
    
    def add_armies(self, graph, player):
        """
        For now add armies randomly
        """
        country = random.choice(list(player.territories))
        graph.nodes[country]["armies"] += 1
        player.armies_available -= 1
        return graph, player



