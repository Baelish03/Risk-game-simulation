import networkx as nx
import matplotlib.pyplot as plt

class Map():
    """
    Defines states, their paths and own details.
    """
    def __init__(self):
        self.world = nx.Graph()
        

    def states(self): 
        """
        Defines states as nodes of a networkx graph
        """
        names = [
            # North America
            "Alaska",
            "Northwest Territory",
            "Greenland",
            "Alberta",
            "Ontario",
            "Quebec",
            "Western United States",
            "Eastern United States",
            "Central America",

            # South America
            "Venezuela",
            "Peru",
            "Brazil",
            "Argentina",

            # Europe
            "Iceland",
            "Scandinavia",
            "Ukraine",
            "Great Britain",
            "Northern Europe",
            "Western Europe",
            "Southern Europe",

            # Africa
            "North Africa",
            "Egypt",
            "East Africa",
            "Congo",
            "South Africa",
            "Madagascar",

            # Asia
            "Ural",
            "Siberia",
            "Yakutsk",
            "Kamchatka",
            "Irkutsk",
            "Mongolia",
            "Japan",
            "Afghanistan",
            "Middle East",
            "India",
            "Siam",
            "China",

            # Australia
            "Indonesia",
            "New Guinea",
            "Western Australia",
            "Eastern Australia"
        ]
        self.world.add_nodes_from(names)   

    def borders(self):
        world = self.world
        

    def plot(self):
        world = self.world
        nx.draw_networkx(self.world, with_labels=True, font_weight='bold')
        plt.show()

mappa = Map()
mappa.states()
mappa.plot()
