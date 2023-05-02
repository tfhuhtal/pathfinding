from time import time
# from PIL import Image, ImageDraw
from algorithms.astar import AStar
from algorithms.dijkstra import Dijkstra
from algorithms.jps import JPS


def main():
    # image = Image.open("map2.png")
    # pixels = image.load()
    # width, height = image.size
    # matrix = [[pixels[j, i] for j in range(width)] for i in range(height)]
    # maze = [[0 if matrix[i][j] == (229, 229, 229, 255)
    #         else 1 for j in range(width)] for i in range(height)]
    #
    # start = (height//9, width//4) #(height//9 + 60, width//2 - 155)  #
    # end = (height//2 +170, width//2 + 125) #(height - 28, width//2 - 340)  #

    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

    start = (0, 0)
    end = (9, 9)

    dijkstra = Dijkstra(maze)
    astar = AStar(maze)
    jps = JPS(maze)

    start_time = time()
    path, operations = jps.search(start, end)
    end_time = time()
    print(f"JPS: {(end_time-start_time)*1000:.2f} ms ({operations} operations)")

    path = [(x, y) for y, x in path]

    # draw = ImageDraw.Draw(image)
    # draw.line(path, fill=(255, 0, 0), width=2)
    # image.save("path_jps.png")

    start_time = time()
    path, operations = astar.search(start, end)
    end_time = time()
    print(f"A*: {(end_time - start_time)*1000:.2f} ms ({operations} operations)")

    start_time = time()
    path = dijkstra.search(start, end)
    end_time = time()
    print(
        f"Dijkstra: {(end_time - start_time)*1000:.2f} ms ({operations} operations)")


if __name__ == "__main__":
    main()
