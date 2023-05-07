from time import time
from PIL import Image
from algorithms.astar import AStar
from algorithms.dijkstra import Dijkstra
from algorithms.jps import JPS

maps = ['map5', 'map5', 'map5', 'map5', 'map5']
starts = [(157, 51), (992, 543), (537, 36), (576, 941), (420, 260)]
ends = [(168, 900), (420, 270), (693, 893), (467, 438), (503, 780)]


def main():

    jps_full = 0
    jps_ops = 0
    astar_full = 0
    astar_ops = 0
    dijkstra_full = 0
    dijkstra_ops = 0

    for i, j in enumerate(maps):

        for _ in range(10):
            image = Image.open(f"maps/{j}.png")
            pixels = image.load()
            width, height = image.size
            matrix = ([[0 if pixels[i, j] == (229, 229, 229, 255) else 1 for i in range(height)]
                       for j in range(width)])

            jps = JPS(matrix)

            start = starts[i]
            end = ends[i]

            jps_start = time()
            res = jps.search(start, end)
            jps_end = time()
            jps_time = jps_end - jps_start
            jps_full += jps_time
            jps_ops += res[1]

        for _ in range(10):
            image = Image.open(f"maps/{j}.png")
            pixels = image.load()
            width, height = image.size
            matrix = ([[0 if pixels[i, j] == (229, 229, 229, 255) else 1 for i in range(height)]
                       for j in range(width)])

            astar = AStar(matrix)

            start = starts[i]
            end = ends[i]

            astar_start = time()
            res = astar.search(start, end)
            astar_end = time()
            astar_time = astar_end - astar_start
            astar_full += astar_time
            astar_ops += res[1]

        for _ in range(10):
            image = Image.open(f"maps/{j}.png")
            pixels = image.load()
            width, height = image.size
            matrix = ([[0 if pixels[i, j] == (229, 229, 229, 255) else 1 for i in range(height)]
                       for j in range(width)])

            dijkstra = Dijkstra(matrix)

            start = starts[i]
            end = ends[i]

            dijkstra_start = time()
            res = dijkstra.search(start, end)
            dijkstra_end = time()
            dijkstra_time = dijkstra_end - dijkstra_start
            dijkstra_full += dijkstra_time
            dijkstra_ops += res[1]

    print(f"JPS: {(jps_full)*1000:.2f} ms, {jps_ops} operations")
    print(f"A*: {(astar_full)*1000:.2f} ms, {astar_ops} operations")
    print(f"Dijkstra: {(dijkstra_full)*1000:.2f} ms, {dijkstra_ops} operations")


if __name__ == '__main__':
    main()
