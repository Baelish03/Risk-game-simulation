import json
import networkx as nx
import matplotlib.pyplot as plt

class WorldMap:
    """
    Defines states, their paths and own details.
    """
    def __init__(self):
        self.world = nx.Graph()
        self.load_from_json("./countries.json")

    def create_nodes(self, continents_data, countries_data):
        """
        Check if nodes in countries' list are the same of continents' list
        """
        for continent_name, continent_data in continents_data.items():
            color = continent_data["color"]

            for country in continent_data["countries"]:
                if country not in countries_data:
                    raise ValueError(f"{country} is in continents but not in countries")

                self.world.add_node(
                    country,
                    continent=continent_name,
                    color=color
                        )
                
    def create_edges(self, countries_data):
        """
        Check if countries in neighbors' list are in nodes.
        After check if edge is already in graph.
        """
        for country_name, country_data in countries_data.items():
            self.world.nodes[country_name]["position"] = tuple(country_data["position"]) 
            for neighbor in country_data["neighbors"]:
                if neighbor not in self.world.nodes:
                    raise ValueError(f"Neighbor {neighbor} not in nodes")
                
                if not self.world.has_edge(country_name, neighbor):
                    self.world.add_edge(country_name, neighbor)

    def owner(self):
        """
        Define player ownership of a node as an attribute and how much soldiers are on it as weight
        """    
        nx.set_node_attributes(self.world, "NonePlayer", "owner")
        nx.set_node_attributes(self.world, 0, "armies")

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
        countries_data = data["countries"]
        continents_data = data["continents"]
        self.create_nodes(continents_data, countries_data)
        self.create_edges(countries_data)
        self.owner()

    def plot(self):
        """
        Plot a beautiful graph of the map
        """
        position = nx.get_node_attributes(self.world, "position")
        node_colors = nx.get_node_attributes(self.world, "color").values()
        label_colors = nx.get_node_attributes(self.world, "label_color")

        nx.draw_networkx(self.world,
                         with_labels=False,
                         font_weight='bold',
                         pos=position,
                         node_color=node_colors,
                         node_size=400,
                         edge_color="black"
                         )

        labels = {
            node: f"{node} \n {self.world.nodes[node]['armies']}"
            for node in self.world.nodes()
            }

        nx.draw_networkx_labels(self.world,
                                pos=position,
                                labels=labels,
                                font_color=label_colors,
                                font_weight="bold")
        plt.axis("off")
        plt.tight_layout()
        plt.show()

