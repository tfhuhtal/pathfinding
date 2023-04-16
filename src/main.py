from time import time
from PIL import Image, ImageDraw
from algorithms.dijkstra import Dijkstra
from algorithms.a_star import AStar

def visualize_path(path, maze):
    for x, row in enumerate(maze):
        for y, col in enumerate(row):
            if (x, y) == path[0]:
                print('A', end=' ')
            elif (x, y) == path[-1]:
                print('B', end=' ')
            elif (x, y) in path:
                print('o', end=' ')
            elif col == 0:
                print('.', end=' ')
            elif col == 1:
                print('#', end=' ')
            else:
                print(col, end=' ')
        print()


def main():

    image = Image.open("den020d.png")
    pixels = image.load()
    width, height = image.size
    matrix = [[pixels[j, i] for j in range(width)] for i in range(height)]
    maze = [[0 if matrix[i][j] == (229, 229, 229, 255) else 1 for j in range(width)] for i in range(height)]
    
    dijkstra = Dijkstra(maze)
    a_star = AStar(maze)

    start = None
    end = None

    for i in range(width):
        if maze[height//9][i] == 0:
            start = (height//9, i)
            break

    for i in range(width):
        if maze[height-100][i] == 0:
            end = (height-100, i)
            break

    start_time = time()
    path = dijkstra.dijkstra(start, end)
    end_time = time()
    opr = dijkstra.get_operations()
    length = dijkstra.distances[end[0]][end[1]]
    print(f"Dijkstra: Path length: {length} Time taken: {(end_time - start_time)*1000:.2f} ms Operations: {opr}")

    start_time = time()
    path = a_star.a_star(start, end)
    end_time = time()
    opr = a_star.operations
    length = a_star.distances[end[0]][end[1]]
    print(f"A*: Path length: {length} Time taken: {(end_time - start_time)*1000:.2f} ms Operations: {opr}")

    path = [(x, y) for y, x in path]

    draw = ImageDraw.Draw(image)
    draw.line(path, fill=(255,0,0),width=1)
    image.save("path.png")


if __name__ == "__main__":
    main()
