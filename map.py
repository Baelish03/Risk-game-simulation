import json
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time

class Map():
    """
    Defines states, their paths and own details.
    """
    def __init__(self):
        self.world = nx.Graph()
        self.load_from_json("./countries.json")

    def load_from_json(self, filename):
        """
        Defines states as nodes and borders as edges of a networkx graph.
        Add two attributes: continent for army reward and color for node color
            for graph plotting. 
        They can be unified but it is easier to create a new attribute instead
            of using color for army reward.
        """
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        for continent_name, continent_data in data["continents"].items():
            print(continent_name, "\n", continent_data)
            color = continent_data["color"]

            for country in continent_data["countries"]:
                self.world.add_node(
                    country,
                    continent=continent_name,
                    color=color
                )


        self.world.add_edges_from(data["borders"])             

    def owner(self):
        """
        Define player ownership of a node as an attribute and how much soldiers are on it as weight
        """    
        pass

    def plot(self):
        """
        Plot a beautiful graph of the map
        """
        world = self.world
        
        pos = dict(zip(self.names, pos))
        node_colors = [world.nodes[n]["color"] for n in world.nodes()]
        
        fig = plt.figure()

        axes = fig.add_subplot(1,1,1)
        nx.draw_networkx(world, with_labels=True, font_weight='bold', pos=pos, node_color=node_colors)
        fig.tight_layout()
        plt.show()

t0 = time.time()
mappa = Map()
print(time.time() - t0)

mappa.plot()

