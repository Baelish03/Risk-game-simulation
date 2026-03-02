import world_map
import time

if "__main__" == __name__:
    start = time.perf_counter()
    world = world_map.WorldMap()
    print(f"Time passed: {time.perf_counter() - start:.4f}s")
    world.plot()