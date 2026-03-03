from world_map import WorldMap
import time
from setup import Setup
from player import Player



if "__main__" == __name__:
    start = time.perf_counter()
    world = WorldMap()
    world_graph = world.world

    POSSIBLE_PLAYERS = [Player("Alan", "#ff0000"), Player("Becca", "#007900"), Player("Charles", "#0000ff"),
                    Player("Diane", "#ffff00"), Player("Emmanuel", "#000000"), Player("Fiona", "#ff00ff")] # better than player1, player2, etc...
    N_OF_PLAYERS = 6
    PLAYERS = POSSIBLE_PLAYERS[:N_OF_PLAYERS] # select a subset from possible players with number of players dimension

    setup = Setup(N_OF_PLAYERS, PLAYERS)

    ordered_players = setup.players_order()

    for player in ordered_players:
        player.armies_available = setup.initial_armies()

    while setup.has_free_territories(world_graph):
        for player in ordered_players:
            if not setup.has_free_territories(world_graph):
                break
            chosen_country = setup.strategy_initial_territory(world_graph)
            setup.assign_initial_territory(world_graph, chosen_country, player)

    for player in ordered_players:
        while player.armies_available > 0:
            setup.add_armies(world_graph, player)

    print(f"Time passed: {time.perf_counter() - start:.4f}s")
    world.plot()