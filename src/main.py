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
    matrix = ([[0 if pixels[i, j] == (229, 229, 229, 255) else 1 for j in range(height)]
               for i in range(width)])

    jps = JPS(matrix)
    astar = AStar(matrix)
    dijkstra = Dijkstra(matrix)

    start = None
    end = None

    pygame.init()
    pygame.display.set_caption("Pathfinding Visualizer")
    screen = pygame.display.set_mode((width, height))
    screen.fill((255, 255, 255))

    bg = pygame.image.load(f"maps/{map_name}.png")

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
    dist = None

    while running:

        # Handle events
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
                    algorithm = None
                    name = None
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
                    dist = None

        screen.blit(bg, (0, 0))

        # Draw the start and end points
        if start is not None:
            pygame.draw.rect(screen, START_COLOR, (start[0], start[1], 8, 8))
        if end is not None:
            pygame.draw.rect(screen, END_COLOR, (end[0], end[1], 8, 8))

        # Find and draw the path
        if start is not None and end is not None and algorithm is not None:
            if algorithm is not jps:
                start_time = time()
                path, operations, dist = algorithm.search(start, end)
                end_time = time()


                if path is not None:
                    for i, j in path:
                        pygame.draw.rect(screen, PATH_COLOR, (i, j, 2, 2))

            else:
                start_time = time()
                path, operations = jps.search(start, end)
                end_time = time()

                if path is not None:
                    for i, j in path:
                        pygame.draw.rect(screen, (255, 50, 255), (i, j, 4, 4))

        # Display the number of operations and the time taken
        operations_text = font.render(
            "Operations: " + str(operations), True, (0, 255, 135))
        time_text = font.render(
            "Time: " + str(round(end_time - start_time, 2)) + "s", True, (0, 255, 135))
        if name is not None:
            algorithm_text = font.render(
                "Algorithm: " + name, True, (0, 255, 135))
            screen.blit(algorithm_text, (0, 60))

        if dist is not None:
            dist_text = font.render(f"Distance: {dist:.5f}", True, (0, 255, 135))
            screen.blit(dist_text, (0, 90))

        screen.blit(operations_text, (0, 0))
        screen.blit(time_text, (0, 30))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
