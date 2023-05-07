from time import time
from PIL import Image, ImageDraw
from algorithms.astar import AStar
from algorithms.dijkstra import Dijkstra
from algorithms.jps import JPS

def main():
    maps = ['map1', 'map2', 'map3', 'map4', 'map5', 'map6', 'map7', 'map8', 'map9']
    starts = [(170, 383), (605, 930), (535, 59),
              (92, 655), (157, 51), (71, 377),
              (58, 541), (495, 640), (746, 399)
        ]
    ends = [(589, 253), (9, 220), (531, 1034),
            (930, 393), (168, 900), (937, 679),
            (687, 691), (568, 974), (28, 542)
        ]

    print("Welcome to the Pathfinding Visualizer!")
    while True:
        try:
            map_name = input("Choose the map you want to use (map1 - map9): ")
            if map_name in ['map1', 'map2', 'map3', 'map4', 'map5', 'map6', 'map7', 'map8', 'map9']:
                break
            else:
                print("Invalid map number. Please try again.")
        except ValueError:
            map_name = 'map1'
            break

    image = Image.open(f"maps/{map_name}.png")
    pixels = image.load()
    width, height = image.size
    matrix = ([[0 if pixels[i, j] == (229, 229, 229, 255) else 1 for i in range(height)]
             for j in range(width)])

    jps = JPS(matrix)
    astar = AStar(matrix)
    dijkstra = Dijkstra(matrix)

    start = None
    end = None

    for i,j in enumerate(maps):
        if map_name == maps[i]:
            start = starts[i]
            end = ends[i]
            break

    jps_start = time()
    jps_path, opr = jps.search(start, end)
    jps_end = time()
    jps_time = jps_end - jps_start
    print(f"JPS: {(jps_time)*1000:.2f} ms, {opr} operations, path length: {len(jps_path)}")

    jps_path = [(j, i) for i, j in jps_path]

    draw = ImageDraw.Draw(image)
    draw.line(jps_path, fill=(255, 0, 0, 255), width=2)

    astar_start = time()
    astar_path, opr = astar.search(start, end)
    astar_end = time()
    astar_time = astar_end - astar_start
    print(f"A*: {(astar_time)*1000:.2f} ms, {opr} operations, path length: {astar.distances[end[0]][end[1]]}")

    astar_path = [(j, i) for i, j in astar_path]

    draw = ImageDraw.Draw(image)
    draw.line(astar_path, fill=(0, 0, 255, 255), width=2)

    image.save(f"maps/{map_name}_result.png")

    dijkstra_start = time()
    dijkstra_path, opr = dijkstra.search(start, end)
    dijkstra_end = time()
    dijkstra_time = dijkstra_end - dijkstra_start
    print(f"Dijkstra: {(dijkstra_time)*1000:.2f} ms,{opr} operations, path length: {dijkstra.distances[end[0]][end[1]]}")

    dijkstra_path = [(j, i) for i, j in dijkstra_path]

    draw = ImageDraw.Draw(image)
    draw.line(dijkstra_path, fill=(0, 255, 0, 255), width=1)

    image.save(f"maps/{map_name}_result.png")


if __name__ == "__main__":
    main()
