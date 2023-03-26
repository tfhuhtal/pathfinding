from dijkstra import Dijkstra
from time import time

def visualize_path(path, maze):
    for x, row in enumerate(maze):
        for y, col in enumerate(row):
            if (x, y) == path[0]:
                print('A', end=' ')
            elif (x, y) == path[-1]:
                print('B', end=' ')
            elif (x, y) in path:
                print('+', end=' ')
            else:
                print(col, end=' ')
        print()

def main():

    maze = [[0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]]
    dijkstra = Dijkstra(maze)

    start = (1, 3)
    end = (9, 9)

    start_time = time()
    path = dijkstra.dijkstra(start, end)
    end_time = time()
    opr = dijkstra.get_operations()
    print(f"{visualize_path(path, maze)} Time taken: {end_time - start_time} Operations: {opr}")

if __name__ == "__main__":
    main()
