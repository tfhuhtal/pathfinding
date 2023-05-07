from time import time
import pygame
from PIL import Image
from algorithms.astar import AStar
from algorithms.dijkstra import Dijkstra
from algorithms.jps import JPS


def main():
    maps = [
        'map1',
        'map2',
        'map3',
        'map4',
        'map5',
        'map6',
        'map7',
        'map8',
        'map9']

    print("Welcome to the Pathfinding Visualizer!"
          + "\nRight click to place the start and end points."
          + "\nPress 'd' to use Dijkstra's algorithm."
          + "\nPress 'a' to use A* algorithm."
          + "\nPress 'j' to use JPS algorithm.")
    while True:
        try:
            map_name = input("Choose the map you want to use (map1 - map9): ")
            if map_name in maps:
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

    pygame.init()
    pygame.display.set_caption("Pathfinding Visualizer")
    screen = pygame.display.set_mode((width, height))
    screen.fill((255, 255, 255))

    PATH_COLOR = (255, 0, 0)
    START_COLOR = (0, 255, 0)
    END_COLOR = (0, 0, 255)

    font = pygame.font.Font(None, 30)

    running = True
    algorithm = None
    name = None
    operations = 0
    start_time = 0
    end_time = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse clicks
                if start is None:
                    start = event.pos
                elif end is None:
                    end = event.pos
                else:
                    start = None
                    end = None
            elif event.type == pygame.KEYDOWN:
                # Handle key presses
                if event.key == pygame.K_d:
                    algorithm = dijkstra
                    name = "Dijkstra"
                elif event.key == pygame.K_a:
                    algorithm = astar
                    name = "A*"
                elif event.key == pygame.K_j:
                    algorithm = jps
                    name = "JPS"

        # Draw the maze
        for i in range(width):
            for j in range(height):
                color = (255, 255, 255) if matrix[i][j] == 0 else (0, 0, 0)
                pygame.draw.rect(screen, color, (i, j, 1, 1))

        # Draw the start and end points
        if start is not None:
            pygame.draw.circle(screen, START_COLOR, start, 5)
        if end is not None:
            pygame.draw.circle(screen, END_COLOR, end, 5)

        # Find and draw the path
        if start is not None and end is not None and algorithm is not None:
            if algorithm is not jps:
                start_time = time()
                path, operations = algorithm.search(start, end)
                end_time = time()

                if path is not None:
                    for i, j in path:
                        pygame.draw.rect(screen, PATH_COLOR, (i, j, 2, 2))

            else:
                start_time = time()
                path, operations = algorithm.search(start, end)
                end_time = time()

                if path is not None:
                    for i, j in path:
                        pygame.draw.rect(screen, (255, 50, 255), (i, j, 4, 4))

        # Display the number of operations and the time taken
        operations_text = font.render(
            "Operations: " + str(operations), True, (0, 255, 0))
        time_text = font.render(
            "Time: " + str(round(end_time - start_time, 2)) + "s", True, (0, 255, 0))
        if name is not None:
            algorithm_text = font.render(
                "Algorithm: " + name, True, (0, 255, 0))
            screen.blit(algorithm_text, (0, 60))

        screen.blit(operations_text, (0, 0))
        screen.blit(time_text, (0, 30))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
