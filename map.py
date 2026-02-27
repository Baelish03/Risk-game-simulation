import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Map():
    """
    Defines states, their paths and own details.
    """
    def __init__(self):
        self.world = nx.Graph()
        self.names = [
            # North America
            "Alaska",                       # 0
            "Northwest Territory",          # 1
            "Greenland",                    # 2
            "Alberta",                      # 3
            "Ontario",                      # 4
            "Quebec",                       # 5
            "Western United States",        # 6
            "Eastern United States",        # 7
            "Central America",              # 8

            # South America
            "Venezuela",                    # 9
            "Peru",                         # 10
            "Brazil",                       # 11
            "Argentina",                    # 12

            # Europe
            "Iceland",                      # 13
            "Scandinavia",                  # 14
            "Ukraine",                      # 15
            "Great Britain",                # 16
            "Northern Europe",              # 17
            "Western Europe",               # 18
            "Southern Europe",              # 19

            # Africa
            "North Africa",                 # 20
            "Egypt",                        # 21
            "East Africa",                  # 22
            "Congo",                        # 23
            "South Africa",                 # 24
            "Madagascar",                   # 25

            # Asia
            "Ural",                         # 26
            "Siberia",                      # 27
            "Yakutsk",                      # 28
            "Kamchatka",                    # 29
            "Irkutsk",                      # 30
            "Mongolia",                     # 31
            "Japan",                        # 32
            "Afghanistan",                  # 33
            "Middle East",                  # 34
            "India",                        # 35
            "Siam",                         # 36
            "China",                        # 37

            # Australia
            "Indonesia",                    # 38
            "New Guinea",                   # 39
            "Western Australia",            # 40
            "Eastern Australia"             # 41
        ]
        

    def states(self): 
        """
        Defines states as nodes of a networkx graph
        """
        self.world.add_nodes_from(self.names)   

    def borders(self):
        world = self.world
        names = self.names
        
        # Alaska 
        world.add_edge(names[0], names[29]) # Kamchatka
        world.add_edge(names[0], names[1]) # NW Territory
        world.add_edge(names[0], names[3]) # Alberta

        # Northwst Territory
        world.add_edge(names[1], names[2]) # Ontario
        world.add_edge(names[1], names[3]) # Alberta
        world.add_edge(names[1], names[4]) # Greenland

        # Greenland
        world.add_edge(names[2], names[4]) # Ontario
        world.add_edge(names[2], names[5]) # Quebec
        world.add_edge(names[2], names[13]) # Iceland

        # Alberta
        world.add_edge(names[3], names[4]) # Ontario
        world.add_edge(names[3], names[6]) # W US

        # Ontario
        world.add_edge(names[4], names[5]) # Quebec
        world.add_edge(names[4], names[6]) # W US
        world.add_edge(names[4], names[7]) # E US

        # Quebec
        world.add_edge(names[5], names[7]) # E US
    
        # W US
        world.add_edge(names[6], names[7]) # E US
        world.add_edge(names[6], names[8]) # Central America

        # E US
        world.add_edge(names[7], names[8]) # Central America

        # Central America
        world.add_edge(names[8], names[9]) # Venezuela

        # Venezuela
        world.add_edge(names[9], names[10]) # Peru
        world.add_edge(names[9], names[11]) # Brazil

        # Peru
        world.add_edge(names[10], names[11]) # Brazil
        world.add_edge(names[10], names[12]) # Argentina

        # Brazil 
        world.add_edge(names[11], names[12]) # Argentina
        world.add_edge(names[11], names[20]) # N Africa

        # Iceland
        world.add_edge(names[13], names[14]) # GB
        world.add_edge(names[13], names[16]) # Scandinavia

        # Scandinavia
        world.add_edge(names[14], names[15]) # Ukraine
        world.add_edge(names[14], names[16]) # GB
        world.add_edge(names[14], names[17]) # N Europe

        # Ukraine
        world.add_edge(names[15], names[17]) # N Europe
        world.add_edge(names[15], names[19]) # S Europe
        world.add_edge(names[15], names[34]) # M E
        world.add_edge(names[15], names[26]) # Ural
        world.add_edge(names[15], names[33]) # Afghanistan


        # GB
        world.add_edge(names[16], names[17]) # W Europe
        world.add_edge(names[16], names[18]) # N Europe

        # N Europe
        world.add_edge(names[17], names[18]) # W Europe
        world.add_edge(names[17], names[19]) # S Europe

        # W Europe
        world.add_edge(names[18], names[19]) # S Europe
        world.add_edge(names[18], names[20]) # N Africa

        # S Europe
        world.add_edge(names[19], names[34]) # M E
        world.add_edge(names[19], names[21]) # Egypt
        world.add_edge(names[19], names[20]) # N Africa

        # N Africa
        world.add_edge(names[20], names[21]) # Egypt
        world.add_edge(names[20], names[22]) # E Africa
        world.add_edge(names[20], names[23]) # Congo

        # Egypt
        world.add_edge(names[21], names[22]) # E Africa
        world.add_edge(names[21], names[34]) # M E

        # E Africa
        world.add_edge(names[22], names[23]) # Congo
        world.add_edge(names[22], names[24]) # S Africa
        world.add_edge(names[22], names[25]) # Madagascar
        world.add_edge(names[22], names[34]) # M E

        # Congo
        world.add_edge(names[23], names[24]) # S Africa

        # S Africa
        world.add_edge(names[24], names[25]) # Egypt

        # Ural 
        world.add_edge(names[26], names[33]) # Afghanistan
        world.add_edge(names[26], names[37]) # China
        world.add_edge(names[26], names[27]) # Siberia

        # Siberia
        world.add_edge(names[27], names[31]) # Mongolia
        world.add_edge(names[27], names[37]) # China
        world.add_edge(names[27], names[30]) # Irkutsk
        world.add_edge(names[27], names[28]) # Yakutsk

        # Yakutsk
        world.add_edge(names[28], names[30]) # Irkutsk
        world.add_edge(names[28], names[29]) # Kamchatka

        # Kamchatka
        world.add_edge(names[29], names[30]) # Irkutsk
        world.add_edge(names[29], names[31]) # Mongolia
        world.add_edge(names[29], names[32]) # Japan

        # Irkutsk
        world.add_edge(names[30], names[31]) # Mongolia
     
        # Mongolia
        world.add_edge(names[31], names[37]) # China
        world.add_edge(names[31], names[32]) # Japan

        # Afghanistan
        world.add_edge(names[33], names[37]) # China
        world.add_edge(names[33], names[35]) # India
        world.add_edge(names[33], names[34]) # M E

        # M E
        world.add_edge(names[34], names[35]) # India

        # India
        world.add_edge(names[35], names[36]) # Siam
        world.add_edge(names[35], names[37]) # China

        # Siam
        world.add_edge(names[36], names[37]) # China
        world.add_edge(names[36], names[38]) # Indonesia

        # Indonesia
        world.add_edge(names[38], names[39]) # N G
        world.add_edge(names[38], names[40]) # W A

        # N G
        world.add_edge(names[39], names[40]) # W A
        world.add_edge(names[39], names[41]) # E A        

        # W A
        world.add_edge(names[40], names[41]) # E A        

        self.world = world

    def continents(self):
        world = self.world
        names = self.names

        continents = ["North America", "South America", "Europe", "Africa", "Asia", "Oceania"]
        for node in names[:9]: 
            world.nodes[node]["continent"] = continents[0]        
        for node in names[9:13]: 
            world.nodes[node]["continent"] = continents[1]   
        for node in names[13:20]: 
            world.nodes[node]["continent"] = continents[2]
        for node in names[20:26]: 
            world.nodes[node]["continent"] = continents[3]
        for node in names[26:38]: 
            world.nodes[node]["continent"] = continents[4]
        for node in names[38:]: 
            world.nodes[node]["continent"] = continents[5]            
        print(world.nodes.data())

    def plot(self):
        world = self.world
        pos = [(1, 0), # alaska
               (2.5, -1), # nw ter
               (5, -1), # greenland
               (2, -2), # alberta
               (3, -2), # ontario
               (4,-2), # quebec
               (2.5, -3), # w us
               (3.5, -2.5), # e us
               (2.5, -4), # cen america
               (3, -5), # venezuela
               (2, -6), # peru
               (4, -6), # brazil
               (3, -8), #argentina
               (6, -1.5), # iceland
               (7, -2), # scandinavia
               (8, -2.5), # ukraine
               (5.5, -3), # GB
               (7, -3.5), # n europe
               (6, -4), # w europe
               (7, -5), # s europe
               (6.5, -6), # n africa
               (7.5, -6), # egypt
               (8, -7), # e africa
               (7, -7), # congo
               (7.5, -8), # s africa
               (8.5, -7.5), # madagascar
               (9, -2), # ural
               (10, -2), # siberia
               (11, -1), # yakutsk
               (12, 0), # kamchatka
               (11, -2), # irkutsk
               (11, -3), # mongolia
               (12, -2.5), # japan
               (9, -3), # afghanistan
               (8, -4.5), # m e
               (9, -4), # india
               (10, -5), # siam
               (10, -4), # china
               (11, -6), # indonesia
               (12, -6.5), # n g
               (11, -7.5), # w a
               (12, -8) # e a
               ]
        pos = dict(zip(self.names, pos))
        
        fig = plt.figure()

        axes = fig.add_subplot(1,1,1)
        nx.draw_networkx(world, with_labels=True, font_weight='bold', pos=pos)
        fig.tight_layout()
        plt.show()

mappa = Map()
mappa.states()
mappa.borders()
mappa.continents()
mappa.plot()
