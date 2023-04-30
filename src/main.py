from time import time
from PIL import Image, ImageDraw
# from algorithms.dijkstra import Dijkstra
from algorithms.astar import AStar
from algorithms.jps import JPS


def main():
    image = Image.open("map1.png")
    pixels = image.load()
    width, height = image.size
    matrix = [[pixels[j, i] for j in range(width)] for i in range(height)]
    maze = [[0 if matrix[i][j] == (229, 229, 229, 255)
             else 1 for j in range(width)] for i in range(height)]

    start = (height//9 + 60, width//2 - 155)  # (height//9, width//4) #
    end = (height - 28, width//2 - 340)  # (height//2 +170, width//2 + 125) #

    # maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    #        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ]
    #
    # start = (0, 0)
    # end = (9, 9)
#
    astar = AStar(maze)
    # dijkstra = Dijkstra(maze)
    jps = JPS(maze)

    path, oper_time, operations = jps.search(start, end)
    print(f"JPS: {(oper_time)*1000:.2f} ms ({operations} operations)")

    path = [(x, y) for y, x in path]

    draw = ImageDraw.Draw(image)
    draw.line(path, fill=(255, 0, 0), width=2)
    image.save("path_jps.png")

    start_time = time()
    path = astar.search(start, end)
    end_time = time()
    opr = astar.operations
    # print(path)
    print(f"A*: {(end_time - start_time)*1000:.2f} ms ({opr} operations)")


if __name__ == "__main__":
    main()
